import argparse
import pandas as pd
from ruamel.yaml import YAML
import os


from utils.utils import get_model_from_args

def get_args_parser():
    parser = argparse.ArgumentParser('', add_help=False)
    parser.add_argument('--qbank', type=str, required=True)
    parser.add_argument('--model', type=str, required=True)
    return parser

def main(args):
    config_root="../config"
    yaml = YAML(typ='rt')
    config = yaml.load(open(os.path.join(config_root, "config.yaml"), 'r'))

    model_name = args.model
    model = get_model_from_args(model_name)

    """ Convert the question bank file into a dataframe """
    qbank_df = pd.read_csv(args.qbank)
    qbank_root = args.qbank[:args.qbank.rfind('/')]

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
    for index, row in qbank_df.iterrows():
        question = f'Question: {row["question"]}\nPossible answers:\na:{row["a"]}\nb:{row["b"]}\nc:{row["c"]}\nd:{row["d"]}\ne:{row["e"]}'
        question_known = -1
        answer = ""
        if row['block'] not in seen_question_blocks and row['block'] != -1 and row['category'] != 'Psychiatry':
            seen_question_blocks.add(row['block'])
            """ Answer the question """
            prompt_task = f"{question}"
            answer = model.chat(prompt=prompt_task, max_token=config['max_tokens'])
            print(answer)
            """ Get the answer in a more uniformed format by asking to extract it from the previous answer"""
            prompt_format_answer = f"Below I provide you with an answer I received to a question I asked to one of my students. It contains also the rationale for the given answer, and I want to extract only the provided answer (which can have values a,b,c,d or e). Please extract the letter provided by the student among a,b,c,d,e. Write only the letter and nothing else. Ignore punctuation as well. \nAnswer:\n{answer}"
            formatted_answer = model.chat(prompt=prompt_format_answer, max_token=config['max_tokens'])
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
    qbank_df[model_name+'-known'] = total_answers
    qbank_df[model_name + '-fullanswer'] = full_answers
    qbank_df.to_csv(os.path.join(qbank_root, "question_bank_with_model_answers.csv"), index=False)



if __name__ == '__main__':
    parser = argparse.ArgumentParser('For the given model, understand for which Multiple-Choice Questions from the given question bank it knows the answer.', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)

