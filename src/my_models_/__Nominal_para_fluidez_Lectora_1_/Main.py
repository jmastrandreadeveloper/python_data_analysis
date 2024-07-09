
import pandas as pd
from src.my_models_._abstract_model_.AbstractMain import AbstractMain
from .GroupAggregation import GroupAggregation
from .Preprocessor import Preprocessor
from .Transform import Transform
import src.tools.utils as u

class Main(AbstractMain):

    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)  
        # acá empiezo con la ejecución 
        self.run_all()

    def run_all(self):
        # Implementar una secuencia de operaciones que utilicen los métodos de las instancias        
        self.preprocessor = Preprocessor(self.dataframe)
        self.df_nominal_processed = self.preprocessor.do_preprocessor()        
        # obtener la lista de las escuelas a analizar buscando en la columna Escuela_ID y devolviendo una lista de ellas
        self.listaEscuelas_IDs = self.preprocessor.obtener_datos_de_columna('Escuela_ID' , True)
        self.group_agg = GroupAggregation(self.df_nominal_processed)
        # para que finalmente sea accedido desde otra parte, desde el reporte
        # porque de este dataframe saldrán los datos institucionales        
        u.save_dataframe_to_csv(self.df_nominal_processed,'data/processed/transformed/Nominal_final_procesado.csv')        
        pass