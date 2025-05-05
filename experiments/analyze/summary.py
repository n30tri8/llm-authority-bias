import os
import pandas as pd
from pathlib import Path
from utils.logger import out_logger, file_logger

def summarize(model_name: str, results_path: Path, first_person: bool):
    summary_file_name = f'{model_name}_summary.csv'
    summary_file_path = results_path / summary_file_name
    columns = ['model', 'profession', 'gender', 'position', 'workplace_study', 'change_ratio', 'first_person']
    if not os.path.exists(summary_file_path):
        df = pd.DataFrame(columns=columns)
        df.to_csv(summary_file_path, index=False)
    else:
        df = pd.read_csv(summary_file_path)
    for filename in os.listdir(results_path):
        if filename.endswith('.csv') and 'summary' not in filename:
            file_path = results_path / filename
            result_df = pd.read_csv(file_path)
            expert_influence = sum([1 if row['expert_answer'] == row['after_exp_m_answer'] else 0 for _,row in result_df.iterrows()])/len(result_df)
            new_row = {
                'model': model_name,
                'profession': result_df['profession'][0],
                'workplace_study': result_df['workplace_study'][0],
                'position': result_df['position'][0],
                'gender': result_df['gender'][0],
                'change_ratio':round(expert_influence,3),
                'first_person': first_person
            }
            new_row = pd.DataFrame([new_row])
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(summary_file_path, index=False)
    log_msg = f"Summary built for the model [{model_name}] and first_person set to [{first_person}].\nThe file can be found at the path: {summary_file_path}"
    file_logger.info(log_msg)
    out_logger.info(log_msg)


def summarize_mmmlu(model_name: str, results_path: Path, first_person: bool):
    summary_file_name = f'{model_name}_mmmlu_summary.csv'
    summary_file_path = results_path / summary_file_name
    columns = [
        'model', 'gender', 'position', 'workplace_study',
        'change_ratio','first_person', 'language', 'subject', 'count'
    ]
    if not os.path.exists(summary_file_path):
        df = pd.DataFrame(columns=columns)
        df.to_csv(summary_file_path, index=False)
    else:
        df = pd.read_csv(summary_file_path)

    for filename in os.listdir(results_path):
        if filename.endswith('.csv') and 'summary' not in filename:
            file_path = results_path / filename
            result_df = pd.read_csv(file_path)

            # Iterate over each combination of language and subject
            for lang in result_df['language'].unique():
                for subject in result_df['subject'].unique():
                    subset = result_df[(result_df['language'] == lang) & (result_df['subject'] == subject)]
                    if len(subset) > 0:
                        change_ratio = sum(
                            subset['expert_answer'] == subset['after_exp_m_answer']
                        ) / len(subset)

                        new_row = {
                            'model': model_name,
                            'workplace_study': subset['workplace_study'].iloc[0],
                            'position': subset['position'].iloc[0],
                            'gender': subset['gender'].iloc[0],
                            'language': lang,
                            'subject': subject,
                            'change_ratio': round(change_ratio, 3),
                            'count': len(subset),
                            'first_person': first_person
                        }
                        new_row = pd.DataFrame([new_row])
                        df = pd.concat([df, new_row], ignore_index=True)

            # Calculate total change_ratio
            total_change_ratio = sum(
                [1 if row['expert_answer'] == row['after_exp_m_answer'] else 0 for _, row in result_df.iterrows()]
            ) / len(result_df)

            new_row = {
                'model': model_name,
                'workplace_study': result_df['workplace_study'][0],
                'position': result_df['position'][0],
                'gender': result_df['gender'][0],
                'language': 'All',
                'subject': 'All',
                'change_ratio': round(total_change_ratio, 3),
                'count': len(result_df),
                'first_person': first_person
            }
            new_row = pd.DataFrame([new_row])
            df = pd.concat([df, new_row], ignore_index=True)

            df.to_csv(summary_file_path, index=False)

    log_msg = f"MMMLU Summary built for the model [{model_name}] and first_person set to [{first_person}].\nThe file can be found at the path: {summary_file_path}"
    file_logger.info(log_msg)
    out_logger.info(log_msg)