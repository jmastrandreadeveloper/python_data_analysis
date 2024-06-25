# src/preprocessing/grouping/group_by_columns.py
import pandas as pd

def group_by_column(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:
    return dataframe.groupby(column)

def group_by_multiple_columns(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
    return dataframe.groupby(columns)
