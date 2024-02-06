# py-scripts/schema-gen/Medgraph Insight
# Project Title: Synthetic Data Generation for Patient Demographics and Stats

## Introduction

This Python script is designed to generate synthetic data for demographics and statistics related to a medical dataset. The data includes information about patients' demographics, co-morbidity, mortality rate, and yearly data for a specific medical condition.
## Purpose

The primary purpose of this script is to provide a tool for generating realistic but synthetic datasets for testing and development purposes. This can be especially useful when working with sensitive or private medical data where sharing the actual data might not be feasible.

## Environment

- Python Version: 3.11
- IDE: Spyder 5.4.3

## Dependencies

- pandas: Data manipulation and analysis library
- numpy: Numerical operations library
- json: JSON encoding and decoding library
- os: Operating system interface for file handling

## How to Run

1. Ensure that Python 3.11 is installed on your system.
2. Install the required dependencies using 
```bash 
pip install pandas numpy
```
3. Open the script in Spyder or any Python IDE of your choice.
4. Run the script.

## User Input - Seed Value

The script prompts the user to enter a seed value. The seed value is used to initialize the random number generator from the NumPy library. Setting a seed ensures that the generated data remains consistent across runs, providing reproducibility.
```console
Enter seed value:
```
## Code Structure

### Demographics Data Generation (dataDemographics.py)

- Reads existing demographic data from 'RA result_300_all_years.xlsx'.
- Generates synthetic data for co-morbidity, mortality rate, and yearly data.
- Utilizes the seed value for reproducibility.
- Outputs a JSON file ('dataDemographics.json') and an Excel file ('dataDemographics.xlsx').

### Stats Data Generation (DemographicsStats.py)

- Reads demographic data from 'dataDemographics.xlsx'.
- Generates synthetic yearly data for each patient.
- Utilizes the seed value for reproducibility.
- Outputs a JSON file ('DemographicsStats.json') and an Excel file ('DemographicsStats.xlsx').

## Output Files

1. **dataDemographics.json**: JSON file containing synthetic demographic data.
2. **dataDemographics.xlsx**: Excel file containing synthetic demographic data.
3. **DemographicsStats.json**: JSON file containing synthetic stats data.
4. **DemographicsStats.xlsx**: Excel file containing synthetic stats data.
## Schema
**Schema for Patient Demographics** <br>
<br>
```json
{
    code: {
      // patient code i.e a string used to categorize but for now we use numbering
      type: String,
      required: true,
      min: 2,
      max: 100,
    },
    age: {
      type: Number,
      required: true,
    },

    gender: {
      type: String,
      enum: ["Male", "Female","Undefined"],
      default: "Undefined",
    },
    smoking: {
      type: String,
      enum: ["Yes", "No"],
      default: "No",
    },
    description: String,
},
  { timestamps: true }
  ```
<br>
**Schema for Demographics Stats**<br>
<br>

```js
{
    yearId: String,
    coMorbidity: Number,
    mortalityrate: Number,
    yearlyData: [
      {
        year: String,
        esr: Number,
        crp: Number,
        dasesr: Number,
        dascrp: Number,
        sdai: Number,
        tj: String,
        sj: Number,
        global: Number,
        haq: String,
        rem: String,
        dasrem: String,
        sdairem: String,
        boorem: String,
      },
    ],
  },
  { timestamps: true } 
  ```

## Demographic stats field definitions used
The specified terms are commonly used in clinical trials, especially in the context of rheumatology and inflammatory diseases. The types specify the data format expected for each variable, and the descriptions provide insights into their clinical significance.

- **esr (Erythrocyte Sedimentation Rate):**
  - Type: Number
  - Description: ESR is a blood test that measures the rate at which red blood cells settle in a test tube. It is a non-specific marker of inflammation and is often used to monitor inflammatory conditions.

- **crp (C-Reactive Protein):**
  - Type: Number
  - Description: CRP is a protein produced by the liver in response to inflammation. Elevated CRP levels in the blood indicate the presence of inflammation in the body.

- **dasesr (Disease Activity Score based on ESR):**
  - Type: Number
  - Description: DASESR is a composite score used to assess disease activity in rheumatoid arthritis. It incorporates the patient's global assessment, the number of tender joints, the number of swollen joints, and the ESR.

- **dascrp (Disease Activity Score based on CRP):**
  - Type: Number
  - Description: DASCRP is similar to DASESR but uses CRP instead of ESR in the calculation. It is another method for assessing disease activity in rheumatoid arthritis.

- **sdai (Simplified Disease Activity Index):**
  - Type: Number
  - Description: SDAI is a composite score that assesses disease activity in rheumatoid arthritis. It includes the tender joint count, swollen joint count, patient's global assessment, and CRP.

- **tj (Tender Joints):**
  - Type: String
  - Description: The number of joints that are tender upon palpation or pressure. Typically assessed in rheumatological examinations.

- **sj (Swollen Joints):**
  - Type: Number
  - Description: The number of joints that show signs of inflammation or swelling. It is an important parameter in assessing joint involvement in diseases like rheumatoid arthritis.

- **global (Global Assessment):**
  - Type: Number
  - Description: The patient's overall assessment of their health or disease status. It is often a subjective measure included in composite scores.

- **haq (Health Assessment Questionnaire):**
  - Type: String
  - Description: HAQ is a questionnaire that assesses the patient's ability to perform daily activities. It is commonly used to evaluate functional status in rheumatic diseases.

- **rem (Remission):**
  - Type: String
  - Description: Indicates whether the patient is in a state of remission, meaning that the symptoms of the disease are minimal or absent.

- **dasrem (DAS Remission):**
  - Type: String
  - Description: Indicates whether the patient is in remission according to the Disease Activity Score criteria.

- **sdairem (SDAI Remission):**
  - Type: String
  - Description: Indicates whether the patient is in remission according to the Simplified Disease Activity Index criteria.

- **boorem (Boolean Remission):**
  - Type: String
  - Description: Indicates whether the patient meets specific criteria for remission based on a set of predefined measures. Often represented as a boolean value.

## Acknowledgments

This script is created as part of a data generation project and is not intended for use with real patient data. Always follow ethical guidelines and regulations when working with medical data.

#### Go to Index [by clicking here](/README.md)
