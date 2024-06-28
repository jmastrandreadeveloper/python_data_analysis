from abc import ABC, abstractmethod
import pandas as pd

class AbstractPreprocessor(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def cleaning_data(self):
        pass

    @abstractmethod
    def filter_data(self):
        pass

    @abstractmethod
    def transform_data(self):
        pass

    @abstractmethod
    def validate_data(self):
        pass

    def método_concreto(self):
        print('este es un método concreto')