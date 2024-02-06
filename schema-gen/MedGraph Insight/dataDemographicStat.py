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
# import uuid #for user id generation

# function to genrate value inside the yearly data array
def generate_data(year):
    return [
        {
            "year": str(2022 - i),
            "esr": str(np.random.randint(1, 50)),
            "crp": str(np.random.uniform(0.0, 50.0)),
            "dasesr": str(np.random.uniform(1.0, 5.0)),
            "dascrp": str(np.random.uniform(1.0, 5.0)),
            "sdai": str(np.random.uniform(10.0, 50.0)),
            "tj": str(np.random.randint(1, 5)),
            "sj": str(np.random.randint(1, 5)),
            "global": str(np.random.randint(1, 5)),
            "haq": str(np.random.randint(2)),  # Generates 0 or 1
            "rem": str(np.random.randint(2)),  # Generates 0 or 1
            "dasrem": str(np.random.randint(2)),  # Generates 0 or 1
            "sdairem": str(np.random.randint(2)),  # Generates 0 or 1
            "boorem": str(np.random.randint(2)),  # Generates 0 or 1
        } for i in range(year)
    ]


# Get the current working directory
current_directory = os.getcwd()

# Assuming 'dataDemographics.xlsx' is in the current directory
demographics_path = os.path.join(current_directory, 'dataDemographics.xlsx')
new_path = current_directory

# Read demographic data from Excel file
df_dat_dem_stat = pd.read_excel(
    demographics_path, sheet_name='Sheet1', header=0)

# Select relevant columns and rename one column
df_dat_dem_stat = df_dat_dem_stat[['Code', '_id']]
df_dat_dem_stat = df_dat_dem_stat.rename(columns={"_id": "yearid"})

# Create new columns for additional data
df_dat_dem_stat['_id'] = ''  # creates a new empty column
df_dat_dem_stat['coMorbidity'] = ''  # creates a new empty column
df_dat_dem_stat['mortalityrate'] = ''  # creates a new empty column
df_dat_dem_stat['yearlyData'] = ''  # creates a new empty column

# Generate synthetic data for 'coMorbidity', 'mortalityrate', and 'yearlyData'
df_dat_dem_stat['coMorbidity'] = np.random.uniform(
    0.0, 2.0, size=len(df_dat_dem_stat))
df_dat_dem_stat['mortalityrate'] = np.random.uniform(
    0.0, 1.0, size=len(df_dat_dem_stat))
df_dat_dem_stat['yearlyData'] = np.random.randint(
    1, 6, size=len(df_dat_dem_stat))


# Apply the function to generate data for each row based on 'yearlyData'
df_dat_dem_stat['yearlyData'] = df_dat_dem_stat['yearlyData'].apply(
    generate_data)

# Generate unique IDs
for i in range(len(df_dat_dem_stat['_id'])):
    random_id = ''.join(np.random.choice(
        list('0123456789abcdef'), len(df_dat_dem_stat['yearid'][0])))
    df_dat_dem_stat.loc[i, '_id'] = random_id

# df_dat_dem_stat['_id'] = [str(uuid.uuid4()) for _ in range(len(df_dat_dem_stat))]

# Convert DataFrame to JSON
result_demStat = df_dat_dem_stat.to_json(orient="records")
parsed_demoStats = loads(result_demStat)

# Define the filename for the output JSON file
new_file = r'DemographicsStats.json'
new_file_path = os.path.join(new_path, new_file)

# Save the generated JSON to the current directory
with open(new_file_path, 'w') as json_file:
    json.dump(parsed_demoStats, json_file, indent=2)

# Define the filename for the output Excel file to pwd
excel_file_name = 'DemographicsStats.xlsx'
excel_file_path = os.path.join(new_path, excel_file_name)

# Save the DataFrame to Excel
df_dat_dem_stat.to_excel(excel_file_path, index=False)
