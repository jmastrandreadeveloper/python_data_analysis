# src/models/specific_dataframe.py
import pandas as pd
from .abstract_dataframe import AbstractDataFrame

class SpecificDataFrame(AbstractDataFrame):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def group_data(self, column):
        return self.dataframe.groupby(column)

    def filter_data(self, column, value):
        return self.dataframe[self.dataframe[column] == value]

    def sum_aggregation(self, grouped, column):
        return grouped[column].sum()

    def mean_aggregation(self, grouped, column):
        return grouped[column].mean()
    
    def imprimir(self):
        print('hola')
        print(self.dataframe)
