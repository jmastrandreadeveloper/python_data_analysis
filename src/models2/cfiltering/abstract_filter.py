from abc import ABC, abstractmethod
import pandas as pd

class AbstractFilter(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def filter_data(self):
        pass
    
    def filter_by_value(dataframe: pd.DataFrame, column: str, value) -> pd.DataFrame:
        return dataframe[dataframe[column] == value]

    def filter_by_values(dataframe: pd.DataFrame, column: str, values: list) -> pd.DataFrame:
        return dataframe[dataframe[column].isin(values)]
    
    def filter_greater_than(dataframe: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
        return dataframe[dataframe[column] > threshold]

    def filter_less_than(dataframe: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
        return dataframe[dataframe[column] < threshold]

    def filter_between(dataframe: pd.DataFrame, column: str, lower_bound: float, upper_bound: float) -> pd.DataFrame:
        return dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]