import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from pathlib import Path
from utils.logger import file_logger, out_logger

def save_to_img(correlation_df: pd.DataFrame, first_person: bool, save_path: Path):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_df, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.xlabel("")
    plt.ylabel("")
    os.makedirs(save_path, exist_ok=True)
    filename = f"correlation{'_firstperson' if first_person else ''}.png"
    save_path = save_path / filename
    plt.savefig(save_path, dpi=300)
    log_msg = f"Correlation matrix image saved to {save_path}"
    file_logger.info(log_msg)
    out_logger.info(log_msg)
    plt.close()


def correlation(first_person: bool, results_path: Path):
    output_file = results_path / "correlation.csv"
    sort_columns = ["gender", "position", "workplace_study"]
    summary_files = [f for f in os.listdir(results_path) if "summary" in f]
    for root, _, files in os.walk(results_path):
        for f in files:
            if "summary" in f:
                summary_files.append(os.path.join(root, f))
    file_dataframes = {}
    for file in summary_files:
        file_path = results_path / file
        df = pd.read_csv(file_path)
        df.sort_values(by=sort_columns, inplace=True)
        df.reset_index(drop=True, inplace=True)
        file_dataframes[file] = df
    correlation_results = []
    for (file1, df1), (file2, df2) in combinations(file_dataframes.items(), 2):
        # Ensure the column 'change_ratio' exists in both DataFrames
        if 'change_ratio' in df1.columns and 'change_ratio' in df2.columns:
            # Align DataFrames on the 'change_ratio' column
            df1_aligned = df1['change_ratio']
            df2_aligned = df2['change_ratio']
            correlation_df = df1_aligned.corr(df2_aligned)
            model1_name = file1.rsplit('/')[-1].replace('_summary.csv', '')
            model2_name = file2.rsplit('/')[-1].replace('_summary.csv', '')
            model1_fp = "_fp" in model1_name
            model2_fp = "_fp" in model2_name
            correlation_results.append({"model1": model1_name.replace('_fp',''),
                                        "model2": model2_name.replace('_fp',''),
                                        "correlation": correlation_df,
                                        "model1_fp": model1_fp,
                                        "model2_fp": model2_fp})
    correlation_results_df = pd.DataFrame(correlation_results)
    correlation_results_df.to_csv(output_file, index=False)
    log_msg = f"Correlation matrix CSV saved to {output_file}"
    file_logger.info(log_msg)
    out_logger.info(log_msg)

    filtered_corr_df = correlation_results_df[(correlation_results_df['model1_fp'] == first_person) & (correlation_results_df['model2_fp'] == first_person)]
    filtered_corr_df = filtered_corr_df.drop(columns=['model1_fp', 'model2_fp'])
    filtered_corr_df = filtered_corr_df.pivot(index="model1", columns="model2", values="correlation")
    filtered_corr_df = filtered_corr_df.astype(float).fillna(1)
    labels = sorted(set(filtered_corr_df.index).union(set(filtered_corr_df.columns)))

    filtered_corr_df = filtered_corr_df.reindex(index=labels, columns=labels)

    for row in labels:
        for col in labels:
            if pd.notna(filtered_corr_df.loc[row, col]):  # If value exists
                filtered_corr_df.loc[col, row] = filtered_corr_df.loc[row, col]
            elif pd.notna(filtered_corr_df.loc[col, row]):  # If reverse exists
                filtered_corr_df.loc[row, col] = filtered_corr_df.loc[col, row]

    for label in labels:
        filtered_corr_df.loc[label, label] = 1

    save_to_img(filtered_corr_df, first_person, results_path)
