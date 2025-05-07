import os
import pandas as pd
import re

from pathlib import Path

def get_results_path(results_root: Path, model_name: str, first_person: bool):
    last_folder_name = f"{model_name}_fp" if first_person else f"{model_name}"
    results_path = results_root / last_folder_name
    return results_path

def create_results_file(results_path):
    """ Create result dataframe """
    columns = [
        'id_q', 'correct_answer', 'expert_answer', 'after_exp_m_answer', 'after_exp_m_fullanswer',
        'name', 'subspecialty', 'workplace_study', 'position',
        'gender',
    ]

    results_df = pd.DataFrame(columns=columns)
    """ We need to create a new results file considering that this is a new experiment and there may be more """
    # Iterate over all files in the directory
    last_exp_id = -1

    if not os.path.exists(results_path):
        os.makedirs(results_path)
    for filename in os.listdir(results_path):
        if not os.path.isfile(os.path.join(results_path, filename)):
            continue
        numbers = re.findall(r'\d+', filename)
        # Convert extracted numbers to integers
        id = int("".join(numbers))
        last_exp_id = id if id > last_exp_id else last_exp_id

    results_file = os.path.join(results_path,
                                    f'results{last_exp_id + 1}.csv')

    if not os.path.exists(results_file):
        # Create the file
        results_df.to_csv(results_file, index=False)
    return results_file
