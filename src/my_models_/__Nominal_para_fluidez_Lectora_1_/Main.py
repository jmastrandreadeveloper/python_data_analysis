
import pandas as pd
from src.my_models_._abstract_model_.AbstractMain import AbstractMain
from .GroupAggregation import GroupAggregation
from .Preprocessor import Preprocessor
from .Transform import Transform

class Main(AbstractMain):

    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
        self.group_agg = GroupAggregation(dataframe)
        self.preprocessor = Preprocessor(dataframe)
        self.transform = Transform(dataframe)
        print('soy el main del nominal ')

    def run_all(self):
        # Implementar una secuencia de operaciones que utilicen los métodos de las instancias
        pass
