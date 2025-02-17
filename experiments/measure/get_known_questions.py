import pandas as pd
import os

def get_known_questions(model, qbank, qbank_root):


    # We want to ignore those questions which are follow-up of other questions for now.
    # In those cases, we just pick the first question of the block
    seen_question_blocks = set()

    total_answers = []
    full_answers = []

    """ Create a temporary file where to save the answers (to prevent issues caused by a poor network connection) """
    tmp_file_path = os.path.join(qbank_root,"tmp_answer_file.txt")
    if not os.path.exists(tmp_file_path):
        # Create the file
        with open(tmp_file_path, 'a'):
            os.utime(tmp_file_path, None)
    for index, row in qbank.iterrows():
        question = {'role':'user', 'content':f'Question: {row["question"]}\nPossible answers:\na:{row["a"]}\nb:{row["b"]}\nc:{row["c"]}\nd:{row["d"]}\ne:{row["e"]}'}
        question_known = -1
        answer = ""
        if row['block'] not in seen_question_blocks and row['block'] != -1 and row['category'] != 'Psychiatry':
            seen_question_blocks.add(row['block'])
            """ Answer the question """
            answer = model.chat(prompt=[question])
            print(answer)
            answer = {'role':'assistant', 'content':answer}
            """ Get the answer in a more uniformed format by asking to extract it from the previous answer"""
            prompt_format_answer = {'role': 'user', 'content': "I'm sorry I didn't understand what was final answer. Please extract the letter corresponding to the answer among a,b,c,d,e. Answer ONLY with the appropriate letter and nothing else."}
            prompt = ([question, answer, prompt_format_answer])
            formatted_answer = model.chat(prompt=prompt)
            print(f'{index}, {formatted_answer}')
            if formatted_answer == row['answer']:
                """ The model provides the correct answer. """
                question_known = True
                total_answers.append(question_known)
                """ Save also the entire answer because it will be used in successive experiments """
                print(answer)
                full_answers.append(answer)

            else:
                question_known = False
                total_answers.append(question_known)
                full_answers.append("")
        else:
            total_answers.append(-1) # It doesn't even try to answer
            full_answers.append("")
        with open(tmp_file_path, 'a') as f:
            f.write(f"<<<<{question_known}>>>>\n")
            f.write(f"{answer if question_known==True else ''}\n")
    qbank[model.model_name+'-known'] = total_answers
    qbank[model.model_name + '-fullanswer'] = full_answers
    qbank.to_csv(os.path.join(qbank_root, "question_bank.csv"), index=False)


