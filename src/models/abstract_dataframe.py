# src/models/abstract_dataframe.py
from abc import ABC, abstractmethod
import pandas as pd

class AbstractDataFrame(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def group_data(self):
        pass

    @abstractmethod
    def filter_data(self):
        pass
