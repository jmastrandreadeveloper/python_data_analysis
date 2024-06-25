# src/preprocessing/grouping/aggregate_functions.py
import pandas as pd

def sum_aggregation(grouped: pd.DataFrame, column: str) -> pd.Series:
    return grouped[column].sum()

def mean_aggregation(grouped: pd.DataFrame, column: str) -> pd.Series:
    return grouped[column].mean()

def custom_aggregation(grouped: pd.DataFrame, agg_dict: dict) -> pd.DataFrame:
    return grouped.agg(agg_dict)
