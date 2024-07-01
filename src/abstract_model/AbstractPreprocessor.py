from abc import ABC, abstractmethod
import pandas as pd

class AbstractPreprocessor(ABC):

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def isnull(self):
        pass

    @abstractmethod
    def notnull(self):
        pass

    @abstractmethod
    def fillna(self, value):
        pass

    @abstractmethod
    def dropna(self):
        pass

    @abstractmethod
    def drop(self, columns, axis):
        pass

    @abstractmethod
    def rename(self, columns):
        pass

    @abstractmethod
    def sort_values(self, by):
        pass

    @abstractmethod
    def sort_index(self):
        pass
