from abc import ABC, abstractmethod
import pandas as pd

class AbstractGroup(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def group_data(self):
        pass

    def group_by_column(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:
        return dataframe.groupby(column)
    
    def group_by_multiple_columns(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
        return dataframe.groupby(columns)