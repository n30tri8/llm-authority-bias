import argparse
import pandas as pd
from ruamel.yaml import YAML
import os
import json

from utils.utils import get_results_path, create_results_file
from experiments.measure.measure import measure
from experiments.measure.get_known_questions import get_known_questions
from backends import get_model

def get_args_parser():
    parser = argparse.ArgumentParser('', add_help=False)
    sub_parsers = parser.add_subparsers(dest="experiment_name")
    measure_parsers = sub_parsers.add_parser("measure")
    measure_parsers.add_argument('--qbank', type=str, required=True)
    measure_parsers.add_argument('--model', type=str, required=True)
    measure_parsers.add_argument('--profession', type=str, default='general neurologist')
    measure_parsers.add_argument('--workplace_study', type=str, default=None)
    measure_parsers.add_argument('--position', type=str, default=None)
    measure_parsers.add_argument('--gender', type=str, default=None)
    measure_parsers.add_argument('--first_person', action='store_true')
    measure_parsers.add_argument('--max_tokens', type=int, default=512)
    measure_parsers.add_argument('--temperature', type=float, default=0)
    measure_parsers.add_argument('--results_folder', type=str, default="results")
    return parser

def main(args):
    model_name = args.model
    model_registry = json.load(open(os.path.join("../backends/model_registry.json"), 'r'))
    model_dict = next((item for item in model_registry if item.get('model_name') == model_name), None)
    gen_args = {
        'max_tokens': args.max_tokens,
        'temperature': args.temperature,
    }
    model = get_model(model_dict, gen_args)

    """ Convert the question bank file into a dataframe """
    qbank_df = pd.read_csv(args.qbank)


    if args.experiment_name == "measure":
        profession = args.profession
        workplace_study = args.workplace_study
        position = args.position
        gender = args.gender
        first_person = args.first_person
        result_path = get_results_path(config['results_root'], model_name, first_person)
        results_file = create_results_file(results_path=result_path)

        # create file to add the model questions, add them to an existing one or do not extract model questions (they already exist)
        if (f'{model_name}-known' not in qbank_df.columns) or (f'{model_name}-fullanswer' not in qbank_df.columns):
            qbank_root = args.qbank[:args.qbank.rfind('/')]
            get_known_questions(model=model, qbank=qbank_df, qbank_root=qbank_root)
        measure(model=model, qbank=qbank_df, profession=profession, workplace_study=workplace_study, position=position, gender=gender, first_person=first_person, results_file=results_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)
