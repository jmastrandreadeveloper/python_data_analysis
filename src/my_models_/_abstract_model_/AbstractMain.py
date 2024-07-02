from abc import ABC, abstractmethod
import pandas as pd

class AbstractMain:

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def run_all(self):
        pass
