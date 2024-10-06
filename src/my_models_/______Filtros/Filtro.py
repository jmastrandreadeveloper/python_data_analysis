import pandas as pd

class Filtro:
    def __init__(self, dataframe_dict):
        self.dataframe_dict = dataframe_dict

    def matricula_por_escuela(self, value):
        df = self.dataframe_dict['nominal_df_Escuela_ID_Alumno_ID_count']
        # Aquí puedes añadir la lógica de filtrado
        
    def desempeno_por_curso(self, value):
        df = self.dataframe_dict['nominal_df_Escuela_ID_Desempeno']
        # Aquí puedes añadir la lógica de filtrado
        
