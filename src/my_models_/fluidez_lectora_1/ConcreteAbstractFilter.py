from AbstractFilter import AbstractFilter
import pandas as pd

class ConcreteAbstractFilter(AbstractFilter):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def filter_data(self):
        pass

