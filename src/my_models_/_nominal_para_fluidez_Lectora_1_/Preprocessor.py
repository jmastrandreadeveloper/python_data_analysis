from src.abstract_model.AbstractPreprocessor import AbstractPreprocessor
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

    ######################################### acá comienzo con mi código #################################
    def fix_columna_edad(self):
        print('...arreglando datos de la columna edad...')
        pass 