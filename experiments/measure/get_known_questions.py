import os
from utils.logger import out_logger, file_logger
from tqdm import tqdm



def get_known_questions(model, qbank, qbank_root):
    tqdm.pandas()
    seen_question_blocks = set()
    total_answers = []
    full_answers = []
    for index, row in tqdm(qbank.iterrows(), total=len(qbank)):
        question = {'role':'user', 'content':f'Question: {row["question"]}\nPossible answers:\na:{row["a"]}\nb:{row["b"]}\nc:{row["c"]}\nd:{row["d"]}\ne:{row["e"]}'}
        if row['block'] not in seen_question_blocks and row['block'] != -1 and row['category'] != 'Psychiatry':
            seen_question_blocks.add(row['block'])
            """ Answer the question """
            raw_answer = model.chat(prompt=[question])
            file_logger.info(f"Question index: {index}: ")
            file_logger.info(f"QUESTION: {question['content']}")
            file_logger.info(f"ANSWER: {raw_answer}")
            answer = {'role':'assistant', 'content':raw_answer}
            """ Get the answer in a more uniformed format by asking to extract it from the previous answer"""
            prompt_format_answer = {'role': 'user', 'content': "I'm sorry I didn't understand what was final answer. Please extract the letter corresponding to the answer among a,b,c,d,e. Answer ONLY with the appropriate letter and nothing else."}
            prompt = ([question, answer, prompt_format_answer])
            formatted_answer = model.chat(prompt=prompt)
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
            total_answers.append(-1) # It doesn't even try to answer
            full_answers.append("")
    qbank[model.model_name+'-known'] = total_answers
    qbank[model.model_name + '-fullanswer'] = full_answers
    qbank.to_csv(os.path.join(qbank_root, "question_bank.csv"), index=False)
    out_logger.info("QBank updated.")


