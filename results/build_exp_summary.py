import argparse
import pandas as pd
import os

def get_args_parser():
    parser = argparse.ArgumentParser('', add_help=False)
    parser.add_argument('--result_folder', type=str, required=True)
    parser.add_argument('--model', type=str, required=True)
    return parser

def main(args):
    directory_path = args.result_folder
    summary_file_name = args.model + '_summary.csv'

    columns = ['model', 'subspecialty', 'gender', 'position', 'workplace_study', 'change_ratio', 'first_person']

    # Check if the file exists
    if not os.path.exists(summary_file_name):
        # Create an empty DataFrame with the specified columns
        df = pd.DataFrame(columns=columns)

        # Save the DataFrame to a CSV file
        df.to_csv(summary_file_name, index=False)
    else:
        df = pd.read_csv(summary_file_name)
    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file is a CSV file
        if filename.endswith('.csv'):
            # Construct the full file path
            file_path = os.path.join(directory_path, filename)

            # Read the CSV file into a pandas DataFrame
            result_df = pd.read_csv(file_path)

            expert_influence = sum([1 if row['expert_answer'] == row['after_exp_m_answer'] else 0 for _,row in result_df.iterrows()])/len(result_df)

            new_row = {
                'model': args.model,
                'subspecialty': result_df['subspecialty'][0],
                'workplace_study': result_df['workplace_study'][0],
                'position': result_df['position'][0],
                'gender': result_df['gender'][0],
                'change_ratio':round(expert_influence,3),
                'first_person': True if 'fp' in file_path else False
            }
            new_row = pd.DataFrame([new_row])

            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(summary_file_name, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)