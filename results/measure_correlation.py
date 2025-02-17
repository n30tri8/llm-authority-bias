import os
import argparse
import pandas as pd
from itertools import combinations

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Avoid wrapping rows

def get_args_parser():
    parser = argparse.ArgumentParser('', add_help=False)
    parser.add_argument('--result_folder', type=str, required=True)
    return parser

def main(args):
    folder_path = args.result_folder

    # Output file
    output_file = "pairwise_correlations.csv"

    # Columns to sort by
    sort_columns = ["gender", "position", "workplace_study"]

    # Collect all CSV files with "summary" in their names
    summary_files = [f for f in os.listdir(folder_path) if "summary" in f and f.endswith(".csv")]

    # Load files into pandas DataFrames
    file_dataframes = {}
    for file in summary_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        # Sort DataFrame by the specified columns
        df.sort_values(by=sort_columns, inplace=True)
        # Reset index to ensure alignment for correlation
        df.reset_index(drop=True, inplace=True)
        file_dataframes[file] = df

    # Compute pairwise correlations
    correlation_results = []
    for (file1, df1), (file2, df2) in combinations(file_dataframes.items(), 2):
        # Ensure the column 'change_ratio' exists in both DataFrames
        if 'change_ratio' in df1.columns and 'change_ratio' in df2.columns:
            # Align DataFrames on the 'change_ratio' column
            df1_aligned = df1['change_ratio']
            df2_aligned = df2['change_ratio']

            print(df1,df2)

            # Compute correlation
            correlation = df1_aligned.corr(df2_aligned)
            correlation_results.append({"model1": file1, "model2": file2, "correlation": correlation})

    # Save results to a new CSV file
    correlation_df = pd.DataFrame(correlation_results)
    correlation_df.to_csv(output_file, index=False)

    print(f"Pairwise correlations saved to {output_file}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser('', parents=[get_args_parser()])
    args = parser.parse_args()
    main(args)