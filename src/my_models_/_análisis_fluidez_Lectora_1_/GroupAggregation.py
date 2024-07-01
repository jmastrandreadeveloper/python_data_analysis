from src.abstract_model.AbstractGroupAggregation import AbstractGroupAggregation
import pandas as pd

class GroupAggregation(AbstractGroupAggregation):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def groupby(self, *args, **kwargs):
        pass

    def agg(self, *args, **kwargs):
        pass

    def pivot_table(self, *args, **kwargs):
        pass

    def agrupar_a(self , columnas , func):
        # acá le mandamos las columnas para que se sepa qué vamos a agrupar
        return