# src/preprocessing/filtering/filter_by_conditions.py
import pandas as pd

def filter_greater_than(dataframe: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    return dataframe[dataframe[column] > threshold]

def filter_less_than(dataframe: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    return dataframe[dataframe[column] < threshold]

def filter_between(dataframe: pd.DataFrame, column: str, lower_bound: float, upper_bound: float) -> pd.DataFrame:
    return dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]
