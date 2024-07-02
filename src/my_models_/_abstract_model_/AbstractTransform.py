from abc import ABC, abstractmethod
import pandas as pd

class AbstractTransform(ABC):

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def apply(self, func):
        pass

    @abstractmethod
    def map(self, func):
        pass

    @abstractmethod
    def applymap(self, func):
        pass

    @abstractmethod
    def astype(self, dtype):
        pass

    @abstractmethod
    def melt(self, id_vars, value_vars):
        pass

    @abstractmethod
    def resample(self, rule):
        pass

    @abstractmethod
    def rolling(self, window):
        pass
