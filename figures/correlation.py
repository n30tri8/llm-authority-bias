import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the CSV file
csv_file = "/home/momentino/PycharmProjects/llm-authority-bias/results/pairwise_correlations.csv"  # Replace with your file path
data = pd.read_csv(csv_file)

# Rename columns to match the new names
data.rename(columns={"row": "model1", "column": "model2", "value": "correlation"}, inplace=True)

# Filter out rows where either model1 or model2 contains "_fp"
filtered_data = data[~data['model1'].str.contains("_fp") & ~data['model2'].str.contains("_fp")].copy()

# Remove unwanted substrings from the labels
filtered_data.loc[:, 'model1'] = filtered_data['model1'].str.replace("_summary.csv", "", regex=False)
filtered_data.loc[:, 'model1'] = filtered_data['model1'].str.replace("-Deepinfra", "", regex=False)
filtered_data.loc[:, 'model2'] = filtered_data['model2'].str.replace("_summary.csv", "", regex=False)
filtered_data.loc[:, 'model2'] = filtered_data['model2'].str.replace("-Deepinfra", "", regex=False)

# Get unique labels for rows and columns
models = sorted(set(filtered_data['model1']).union(filtered_data['model2']))

# Create a square DataFrame with 1.0 on the diagonal
correlation_matrix = pd.DataFrame(1.0, index=models, columns=models)

# Populate the matrix with the correlations from the CSV
for _, row in filtered_data.iterrows():
    model1 = row['model1']
    model2 = row['model2']
    correlation = row['correlation']
    correlation_matrix.loc[model1, model2] = correlation
    correlation_matrix.loc[model2, model1] = correlation  # Ensure symmetry

# Create the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,          # Display the values in the cells
    fmt=".2f",           # Format the values to 2 decimal places
    cmap="coolwarm",     # Use a coolwarm colormap
    cbar=True,           # Add a colorbar
    xticklabels=True,    # Show the x-axis tick labels
    yticklabels=True     # Show the y-axis tick labels
)

# Remove x and y axis labels
plt.xlabel("")
plt.ylabel("")

# Rotate tick labels for better visibility
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0, va="center")

# Adjust layout to avoid label overlap
plt.tight_layout()

# Display the heatmap
plt.show()


