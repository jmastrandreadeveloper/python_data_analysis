from src.abstract_model.AbstractAgg import AbstractAgg
import pandas as pd

class Agg(AbstractAgg):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def agg_data(self):
        pass

