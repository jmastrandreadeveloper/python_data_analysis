from src.abstract_model.AbstractPreprocessor import AbstractPreprocessor
import pandas as pd

class Preprocessor(AbstractPreprocessor):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def cleaning_data(self):
        pass

    def filter_data(self):
        pass

    def transform_data(self):
        pass

    def validate_data(self):
        pass

