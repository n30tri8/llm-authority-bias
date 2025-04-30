import argparse
import pandas as pd
import json
import os

from experiments.analyze.correlation import correlation
from utils.utils import get_results_path, create_results_file
from utils.logger import file_logger, out_logger
from experiments.measure.measure import measure
from experiments.measure.get_known_questions import get_known_questions, get_qbank_known_dir, get_known_questions_mmmlue
from experiments.analyze.summary import summarize
from backends import get_model
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

def get_args_parser():
    parser = argparse.ArgumentParser('', add_help=False)
    sub_parsers = parser.add_subparsers(dest="command_name")

    measure_parsers = sub_parsers.add_parser("extract-known")
    measure_parsers.add_argument('--qbank', type=str, required=True)
    measure_parsers.add_argument('--benchmark_format', type=str, required=True)
    measure_parsers.add_argument('--model', type=str, required=True)
    measure_parsers.add_argument('--max_tokens', type=int, default=512)
    measure_parsers.add_argument('--temperature', type=float, default=0)

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
    measure_parsers.add_argument('--results_path', type=str, default="results", help="Relative path starting from the project root")

    summarize_parsers = sub_parsers.add_parser("summarize")
    summarize_parsers.add_argument('--model', type=str, required=True)
    summarize_parsers.add_argument('--results_path', type=str, default="results", help="Relative path starting from the project root")
    summarize_parsers.add_argument('--first_person', action='store_true')

    correlation_compute = sub_parsers.add_parser("correlation")
    correlation_compute.add_argument('--results_path', type=str, default="results", help="Relative path starting from the project root")
    correlation_compute.add_argument('--first_person', action='store_true')
    return parser

def load_model(model_name, max_tokens, temperature):
    model_registry = json.load(open(PROJECT_ROOT / "backends/model_registry.json", 'r'))
    model_dict = next((item for item in model_registry if item.get('model_name') == model_name), None)
    gen_args = {
        'max_tokens': max_tokens,
        'temperature': temperature,
    }
    model = get_model(model_dict, gen_args)
    return model


def main(args):
    if args.command_name == "extract-known":
        model_name = args.model
        max_tokens = args.max_tokens
        temperature = args.temperature
        log_msg = f"Loading model from registry with name {model_name}"
        file_logger.info(log_msg)
        out_logger.info(log_msg)
        model = load_model(model_name, max_tokens, temperature)

        benchmark_format = args.benchmark_format

        if benchmark_format == "mmmlu":
            get_known_questions_mmmlue(model, args.qbank)
        elif benchmark_format == "neurology board examples":
            get_known_questions(model, args.qbank)

        log_msg = f"The questions known by the model were extracted."
        file_logger.info(log_msg)
        out_logger.info(log_msg)

    if args.command_name == "measure":
        model_name = args.model
        max_tokens = args.max_tokens
        temperature = args.temperature
        model = load_model(model_name, max_tokens, temperature)
        log_msg = f"Loading model from registry with name {model_name}"
        file_logger.info(log_msg)
        out_logger.info(log_msg)

        """ Convert the question bank file into a dataframe """
        qbank_known_dir = get_qbank_known_dir(model_name, args.qbank)
        qbank_df = pd.read_csv(qbank_known_dir)
        if (f'{model_name}-known' not in qbank_df.columns) or (f'{model_name}-fullanswer' not in qbank_df.columns):
            log_msg = f"I cannot find the known questions or the log of the answer provided by models to such questions. Extract them first."
            file_logger.info(log_msg)
            out_logger.info(log_msg)
            raise ValueError("The model does not know the questions. Please run the extract-known command first.")

        profession = args.profession
        workplace_study = args.workplace_study
        position = args.position
        gender = args.gender
        first_person = args.first_person
        results_root = PROJECT_ROOT / args.results_path
        result_path = get_results_path(results_root, model_name, first_person)
        results_file = create_results_file(results_path=result_path)
        log_msg = f"Running the experiment with cognitive authority defined as: job: [{profession}], work/study place: [{workplace_study}], position: [{position}], gender: [{gender}] "
        file_logger.info(log_msg)
        out_logger.info(log_msg)
        log_msg = f"First person? [{first_person}]"
        file_logger.info(log_msg)
        out_logger.info(log_msg)

        measure(model=model, qbank=qbank_df, profession=profession, workplace_study=workplace_study, position=position, gender=gender, first_person=first_person, results_file=results_file)
        log_msg = "Experiment completed."
        file_logger.info(log_msg)
        out_logger.info(log_msg)
    elif args.command_name == "summarize":
        model_name = args.model
        first_person = args.first_person
        results_root = PROJECT_ROOT / args.results_path
        result_path = get_results_path(results_root, model_name, first_person)
        summarize(model_name=model_name, results_path=result_path, first_person=first_person)
    elif args.command_name == "correlation":
        results_path = PROJECT_ROOT / args.results_path
        if not os.path.exists(results_path):
            os.makedirs(results_path)
        correlation(results_path=results_path, first_person=args.first_person)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)
