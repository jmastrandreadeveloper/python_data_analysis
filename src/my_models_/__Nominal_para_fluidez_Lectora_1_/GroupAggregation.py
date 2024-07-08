from src.my_models_._abstract_model_.AbstractGroupAggregation import AbstractGroupAggregation
import pandas as pd
import os
from src.generator_groups import generate_group_aggregation_class

class GroupAggregation(AbstractGroupAggregation):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
        # generando los grupos que serán comunes a ambos dataframes
        # group_params_list = [
        #     (['Escuela_ID'],{'Alumno_ID': 'count'},{'reset_index': True}),
        #     (['Escuela_ID', 'CURSO_NORMALIZADO'],{'Alumno_ID': 'count'},{'reset_index': True}),
        #     (['Escuela_ID','CURSO_NORMALIZADO','División'],{'Alumno_ID': 'count'},{'reset_index': True}),
            
        #     (['Nivel_Unificado','CURSO_NORMALIZADO'],{'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Supervisión','CURSO_NORMALIZADO'],{'Alumno_ID':'count'}, {'reset_index': True}),

        # ]
        # generate_group_aggregation_class(group_params_list , os.path.dirname(os.path.abspath(__file__)),'GroupAggregationNominal')
        print('agrupando nominal')
        self.groupby()

    def groupby(self, *args, **kwargs):        
        # agrupamientos que salen de la clase abstracta dado que son comunes para los dos dataframes
        self._df_Escuela_ID_Alumno_ID_count = self.df_Escuela_ID_Alumno_ID_count()
        self._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count()
        self._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count()
        self._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count()
        self._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count()
        pass

    def agg(self, *args, **kwargs):
        pass

    def pivot_table(self, *args, **kwargs):
        pass