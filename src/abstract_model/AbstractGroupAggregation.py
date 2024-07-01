from abc import ABC, abstractmethod
import pandas as pd

class AbstractGroupAggregation(ABC):

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def groupby(self, columns):
        pass

    @abstractmethod
    def agg(self, agg_dict):
        pass

    @abstractmethod
    def pivot_table(self, index, columns, values):
        pass
