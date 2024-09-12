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
        question = f'Question: {row["question"]}\nPossible answers:\na:{row["a"]}\nb:{row["b"]}\nc:{row["c"]}\nd:{row["d"]}\ne:{row["e"]}'
        question_known = -1
        answer = ""
        if row['block'] not in seen_question_blocks and row['block'] != -1 and row['category'] != 'Psychiatry':
            seen_question_blocks.add(row['block'])
            """ Answer the question """
            prompt_task = f"{question}"
            answer = model.chat(prompt=prompt_task)
            print(answer)
            """ Get the answer in a more uniformed format by asking to extract it from the previous answer"""
            prompt_format_answer = f"Below I provide you with an answer I received to a question I asked to one of my students. It contains also the rationale for the given answer, and I want to extract only the provided answer (which can have values a,b,c,d or e). Please extract the letter provided by the student among a,b,c,d,e. Write only the letter and nothing else. Ignore punctuation as well. \nAnswer:\n{answer}"
            formatted_answer = model.chat(prompt=prompt_format_answer)
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


