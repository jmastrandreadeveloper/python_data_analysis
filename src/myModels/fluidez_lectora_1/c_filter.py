import pandas as pd
from src.models2.cfiltering.abstract_filter import AbstractFilter

class Filter(AbstractFilter):  
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def filter_data(self):
        return 'filter'
        