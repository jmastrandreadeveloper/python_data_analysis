from abc import ABC, abstractmethod
import pandas as pd

class AbstractAgg(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe    

    @abstractmethod
    def agg_data(self):
        pass
    
    def sum_aggregation(grouped: pd.DataFrame, column: str) -> pd.Series:
        return grouped[column].sum()

    def mean_aggregation(grouped: pd.DataFrame, column: str) -> pd.Series:
        return grouped[column].mean()

    def custom_aggregation(grouped: pd.DataFrame, agg_dict: dict) -> pd.DataFrame:
        return grouped.agg(agg_dict)