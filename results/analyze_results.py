import argparse
import pandas as pd
def get_args_parser():
    parser = argparse.ArgumentParser('', add_help=False)
    parser.add_argument('--result_file', type=str, required=True)
    return parser

def main(args):
    result_file = args.result_file
    result_df = pd.read_csv(result_file)
    expert_influence = sum([1 if row['expert_answer'] == row['after_exp_m_answer'] else 0 for _,row in result_df.iterrows()])/len(result_df)

    print("The model matched the expert answer with a ratio of ",expert_influence)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)