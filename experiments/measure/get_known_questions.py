import os

from tqdm import tqdm

from utils.logger import out_logger, file_logger


def get_qbank_known_dir(model_name, qbank):
    filename = f'qbank_known_{model_name}.csv'
    qbank_root = qbank[:qbank.rfind('/')]
    dir_name = os.path.join(qbank_root, filename)
    return dir_name


def get_known_questions(model, qbank_dir):
    qbank = pd.read_csv(qbank_dir)
    tqdm.pandas()
    seen_question_blocks = set()
    total_answers = []
    full_answers = []
    for index, row in tqdm(qbank.iterrows(), total=len(qbank),
                           desc="Assessing model's perfromance on the question bank"):
        question = {'role': 'user',
                    'content': f'Question: {row["question"]}\nPossible answers:\na:{row["a"]}\nb:{row["b"]}\nc:{row["c"]}\nd:{row["d"]}\ne:{row["e"]}'}
        if row['block'] not in seen_question_blocks and row['block'] != -1 and row['category'] != 'Psychiatry':
            seen_question_blocks.add(row['block'])
            """ Answer the question """

            try:
                raw_answer = model.chat(prompt=[question])
            except Exception as e:
                out_logger.error(f"Error while prompting question {index}; {question}: {e}")
                file_logger.error(f"Error while prompting question {index}; {question}: {e}")
                total_answers.append(-1)  # It doesn't even try to answer
                full_answers.append("")
                continue

            file_logger.info(f"Question index: {index}: ")
            file_logger.info(f"QUESTION: {question['content']}")
            file_logger.info(f"ANSWER: {raw_answer}")
            answer = {'role': 'assistant', 'content': raw_answer}
            """ Get the answer in a more uniformed format by asking to extract it from the previous answer"""
            prompt_format_answer = {'role': 'user',
                                    'content': "I'm sorry I didn't understand what was final answer. Please extract the letter corresponding to the answer among a,b,c,d,e. Answer ONLY with the appropriate letter and nothing else."}
            prompt = ([question, answer, prompt_format_answer])

            try:
                formatted_answer = model.chat(prompt=prompt)
            except Exception as e:
                out_logger.error(f"Error while second prompting question {index}; {question}: {e}")
                file_logger.error(f"Error while second prompting question {index}; {question}: {e}")
                total_answers.append(-1)  # It doesn't even try to answer
                full_answers.append("")
                continue

            if formatted_answer == row['answer']:
                """ The model provides the correct answer. """
                question_known = True
                total_answers.append(question_known)
                """ Save also the entire answer because it will be used in successive experiments """
                full_answers.append(raw_answer)

            else:
                question_known = False
                total_answers.append(question_known)
                full_answers.append("")
        else:
            total_answers.append(-1)  # It doesn't even try to answer
            full_answers.append("")
    qbank[model.model_name + '-known'] = total_answers
    qbank[model.model_name + '-fullanswer'] = full_answers
    qbank_known_dir = get_qbank_known_dir(model.model_name, qbank_dir)
    qbank.to_csv(qbank_known_dir, index=False)
    out_logger.info("QBank updated.")


import pandas as pd
import glob


def read_and_filter_question_banks(qbank_dir, categories_filter=None):
    """
    Read all CSV files in the qbank_dir, filter by categories, and combine into a single dataframe.

    Args:
        qbank_dir: Directory containing question bank CSV files
        categories_filter: List of categories to include (if None, include all)

    Returns:
        Combined pandas DataFrame with a language column
    """
    all_dataframes = []
    csv_files = glob.glob(os.path.join(qbank_dir, "*.csv"))

    for file_path in csv_files:
        # Extract language from filename (e.g., "AR.csv" -> "AR")
        filename = os.path.basename(file_path)
        language = filename.split(".")[0]

        # Read the CSV file
        df = pd.read_csv(file_path)

        df.rename(columns={df.columns[0]: "question_id"}, inplace=True)

        # Add language column
        df['language'] = language

        # Filter by categories if specified
        if categories_filter:
            df = df[df['Subject'].isin(categories_filter)]

        all_dataframes.append(df)

    # Combine all dataframes
    if all_dataframes:
        return pd.concat(all_dataframes, ignore_index=True)
    else:
        return pd.DataFrame()


def get_known_questions_mmmlue(model, qbank_dir):
    tqdm.pandas()
    total_answers = []
    full_answers = []

    # Define the categories to filter
    categories_to_include = ["medical_genetics", "management", "jurisprudence", "sociology"]

    # Read and combine question banks
    qbank = read_and_filter_question_banks(qbank_dir, categories_to_include)


    prompt_store = {
        'ask for precise answer': {
            'EN': "I'm sorry I didn't understand what was final answer. Please extract the letter corresponding to the answer among A,B,C,D. Answer ONLY with the appropriate letter and nothing else.",
            'AR': "عذرًا، لم أفهم الإجابة النهائية. يُرجى استخراج الحرف المقابل للإجابة من بين أ، ب، ج، د. أجب بالحرف المناسب فقط، ولا شيء غيره.",
            'DE': "Es tut mir leid, ich habe die endgültige Antwort nicht verstanden. Bitte entnehmen Sie den Buchstaben aus A, B, C und D, der der Antwort entspricht. Antworten Sie NUR mit dem entsprechenden Buchstaben und sonst nichts.",
            'IT': "Mi dispiace, non ho capito qual era la risposta finale. Per favore, estrai la lettera corrispondente alla risposta tra A, B, C, D. Rispondi SOLO con la lettera appropriata e nient'altro.",
            'HI': "मुझे खेद है कि मैं समझ नहीं पाया कि अंतिम उत्तर क्या था। कृपया A,B,C,D में से उत्तर के संगत अक्षर निकालें। केवल उचित अक्षर से ही उत्तर दें, अन्य किसी अक्षर से नहीं।",
            'JA': "申し訳ありませんが、最終的な答えが理解できませんでした。A、B、C、Dの中から答えに該当する文字を抽出してください。適切な文字のみを答えてください。",
        },
        'possible answers': {
            'EN': "Possible answers",
            'AR': "إجابات ممكنة",
            'DE': "Mögliche Antworten",
            'IT': "Risposte possibili",
            'HI': "संभावित उत्तर",
            'JA': "考えられる回答",
        }

    }

    for index, row in tqdm(qbank.iterrows(), total=len(qbank),
                           desc="Assessing model's perfromance on the question bank"):
        question_language = row['language']
        question = {'role': 'user',
                    'content': f'{row["Question"]}\n{prompt_store["possible answers"][question_language]}:\nA:{row["A"]}\nB:{row["B"]}\nC:{row["C"]}\nD:{row["D"]}'}
        try:
            raw_answer = model.chat(prompt=[question])
        except Exception as e:
            out_logger.error(f"Error while prompting question {index}; {question}: {e}")
            file_logger.error(f"Error while prompting question {index}; {question}: {e}")
            total_answers.append(-1)  # It doesn't even try to answer
            full_answers.append("")
            continue

        file_logger.info(f"Question index: {index}: ")
        file_logger.info(f"QUESTION: {question['content']}")
        file_logger.info(f"ANSWER: {raw_answer}")
        answer = {'role': 'assistant', 'content': raw_answer}
        """ Get the answer in a more uniformed format by asking to extract it from the previous answer"""
        prompt_format_answer = {'role': 'user',
                                'content': prompt_store['ask for precise answer'][question_language]}
        prompt = ([question, answer, prompt_format_answer])

        try:
            formatted_answer = model.chat(prompt=prompt)
        except Exception as e:
            out_logger.error(f"Error while second prompting question {index}; {question}: {e}")
            file_logger.error(f"Error while second prompting question {index}; {question}: {e}")
            total_answers.append(-1)  # It doesn't even try to answer
            full_answers.append("")
            continue

        if formatted_answer == row['Answer']:
            """ The model provides the correct answer. """
            question_known = True
            total_answers.append(question_known)
            """ Save also the entire answer because it will be used in successive experiments """
            full_answers.append(raw_answer)

        else:
            question_known = False
            total_answers.append(question_known)
            full_answers.append("")

    qbank[model.model_name + '-known'] = total_answers
    qbank[model.model_name + '-fullanswer'] = full_answers
    qbank_known_dir = get_qbank_known_dir(model.model_name, qbank_dir)
    qbank.to_csv(qbank_known_dir, index=False)
    out_logger.info("QBank updated.")
