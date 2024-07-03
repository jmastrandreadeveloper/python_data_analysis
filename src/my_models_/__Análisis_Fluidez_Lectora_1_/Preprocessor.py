from src.my_models_._abstract_model_.AbstractPreprocessor import AbstractPreprocessor
import pandas as pd

class Preprocessor(AbstractPreprocessor):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def isnull(self, *args, **kwargs):
        pass

    def notnull(self, *args, **kwargs):
        pass

    def fillna(self, *args, **kwargs):
        pass

    def dropna(self, *args, **kwargs):
        pass

    def drop(self, *args, **kwargs):
        pass

    def rename(self, *args, **kwargs):
        pass

    def sort_values(self, *args, **kwargs):
        pass

    def sort_index(self, *args, **kwargs):
        pass

    def clean_dataframe(self , dataframe, int_columns, float_columns):
        for col in int_columns:
            dataframe[col] = dataframe[col].astype(int).round(0).fillna(0)
        for col in float_columns:
            dataframe[col] = dataframe[col].round(2).fillna(0)
            
        return dataframe