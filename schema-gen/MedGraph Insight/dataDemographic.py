"""
Created on Tue Feb 6 2024

@author: adhistark
"""
# Importing necessary libraries
import pandas as pd
import numpy as np
from json import loads
import json
import os

# Function to fill 'Description' column
def fill_dscrp(row):
    if not row['Description']:
        np.random.seed(seed_value)  # Set seed for random number generation
        value = np.random.randint(1, 5)
        if value == 1:
            row['Description'] = [1]
        else:
            unique_values = set([value])
            additional_values = list(np.random.choice([2, 3, 4, 5], np.random.randint(1, 4), replace=False))
            unique_values.update(additional_values)
            row['Description'] = list(unique_values)
    return row

# Set the current directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# File paths
file_name = "RA result_300_all_years.xlsx"
file_path = os.path.join(script_directory, file_name)
new_path = script_directory

# Get seed value as input
seed_value = int(input("Enter seed value: "))
np.random.seed(seed_value)  # Set seed for NumPy random number generator

# Read Excel file into a DataFrame
df_randomized = pd.read_excel(file_path, sheet_name='Sheet1', header=0)

# Extract relevant columns for demographics
df_demographics = df_randomized.loc[:, ['Code', 'Age', 'Gender', 'Smoking']]

# Create an empty 'Description' column
df_demographics['Description'] = ''

# Apply the fill_dscrp function using loc
df_demographics.loc[:, :] = df_demographics.apply(fill_dscrp, axis=1)

# Map numeric values to corresponding illness descriptions
illness_dscrp = {1: 'No known illness', 2: 'Hypertension', 3: 'Diabetes', 4: 'Arthritis', 5: 'Cardio bypass'}
df_demographics['Description'] = df_demographics['Description'].apply(lambda x: [illness_dscrp[i] for i in x])

# Join descriptions for each row
df_demographics['Description'] = df_demographics['Description'].apply(lambda x: x[0] if x[0] == 'No known illness' else 'History of ' + ', '.join(map(str, x)))

# Create a new column '_id' with specified values for the first 6 rows
df_demographics['_id'] = ''
df_demographics.loc[:5, '_id'] = ['63701d24f03239c72c00018e', '63701d24f03239c72c00018f', '63701d24f03239c72c000190', '63701d24f03239c72c000191', '63701d24f03239867500012a', '63701d24f03239867500012b']

# Generate random IDs for the rest of the rows
for i in range(6, 300):
    random_id = ''.join(np.random.choice(list('0123456789abcdef'), len(df_demographics['_id'].iloc[0])))
    df_demographics.loc[i, '_id'] = random_id

# Convert DataFrame to JSON
result_demographics = df_demographics.to_json(orient="records")
parsed_demographics = loads(result_demographics)

# Save JSON file in the current directory
new_file = 'dataDemographics.json'
new_file_path = os.path.join(new_path, new_file)
with open(new_file_path, 'w') as json_file:
    json.dump(parsed_demographics, json_file, indent=2)

# Export DataFrame to Excel in the current directory
df_demographics.to_excel(os.path.join(new_path, 'dataDemographics.xlsx'), index=False)

