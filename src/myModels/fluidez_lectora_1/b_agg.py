import pandas as pd
from src.models2.bgrouping.abstract_agg import AbstractAgg

class Agg(AbstractAgg):  
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def agg_data(self):
        return 'agg'