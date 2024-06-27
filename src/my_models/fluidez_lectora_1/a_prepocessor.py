import pandas as pd
from src._abstract_model.apreprocessing.abstract_preprocessor import AbstractPreprocessor

class Preprocessor(AbstractPreprocessor):  
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
    
    def cleaning_data(self):
        return 'clean'
    
    def filter_data(self):
        return 'filter'
    
    def transform_data(self):
        return 'transform'
    
    def validate_data(self):
        return 'validate'