import pandas as pd
import numpy as np

def create_age_reference(dataframe: pd.DataFrame) -> dict:
    
    """
    usar un diccionario que pueda servir como referencia
    """
    
    age_reference = {}
    grouped = dataframe.groupby(['CURSO_NORMALIZADO', 'Nivel'])['Edad']
    
    for (curso, nivel), ages in grouped:
        valid_ages = ages[ages > 0]  # Consider only valid ages
        if not valid_ages.empty:
            age_range = (valid_ages.min(), valid_ages.max())
            age_reference[(curso, nivel)] = age_range

    return age_reference

def validate_data(dataframe: pd.DataFrame):
    print("Validating data...")
    
    # Check for missing values
    if dataframe.isnull().sum().sum() > 0:
        print("Validation failed: Missing values found.")
        return False, dataframe
    
    # Ensure 'Edad' column is numeric and convert it to int64
    dataframe['Edad'] = pd.to_numeric(dataframe['Edad'], errors='coerce')
    
    # Example: Check for specific column data types
    expected_dtypes = {        
        'Edad': 'float64'  # Temporarily set to float64 for initial processing
    }
    
    for column, dtype in expected_dtypes.items():
        if column in dataframe.columns and dataframe[column].dtype != dtype:
            print(f"Validation failed: Column '{column}' has incorrect type. Expected {dtype}, got {dataframe[column].dtype}.")
            return False, dataframe

    # Create age reference based on the dataframe
    age_reference = create_age_reference(dataframe)

    # Function to assign an approximate age
    def get_approximate_age(row):
        key = (row['CURSO_NORMALIZADO'], row['Nivel'])
        if key in age_reference:
            return np.mean(age_reference[key])
        return np.nan  # Or some other default value

    invalid_ages_mask = (dataframe['Edad'] <= 0) | (dataframe['Edad'].isna())
    if invalid_ages_mask.any():
        dataframe.loc[invalid_ages_mask, 'Edad'] = dataframe[invalid_ages_mask].apply(get_approximate_age, axis=1)
    
    # Convert ages to int64 after correction
    dataframe['Edad'] = dataframe['Edad'].round().astype('Int64')
    
    # Re-check for invalid ages after correction
    if (dataframe['Edad'] <= 0).any():
        print("Validation failed: Invalid ages found after correction.")
        return False, dataframe    
    
    # Example: Check for duplicate rows
    if dataframe.duplicated().sum() > 0:
        print("Validation failed: Duplicate rows found.")
        duplicated_rows = dataframe[dataframe.duplicated()]
        print(duplicated_rows)
        dataframe.drop_duplicates(inplace=True)
        print("Duplicate rows removed.")
    
    print("Data validation passed.")
    return True, dataframe