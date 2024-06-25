# src/preprocessing/filtering/filter_by_value.py
import pandas as pd

def filter_by_value(dataframe: pd.DataFrame, column: str, value) -> pd.DataFrame:
    return dataframe[dataframe[column] == value]

def filter_by_values(dataframe: pd.DataFrame, column: str, values: list) -> pd.DataFrame:
    return dataframe[dataframe[column].isin(values)]
