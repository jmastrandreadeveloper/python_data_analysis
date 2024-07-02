from src.my_models_._abstract_model_.AbstractGroupAggregation import AbstractGroupAggregation
import pandas as pd
import os
from src.generator_groups import generate_group_aggregation_class

class GroupAggregation(AbstractGroupAggregation):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
        # # generando los grupos que serán comunes a ambos dataframes
        # group_params_list = [
        #     (['Escuela_ID'],{'Alumno_ID': 'count'},{'reset_index': False}),
        #     (['Escuela_ID', 'CURSO_NORMALIZADO'],{'Alumno_ID': 'count'},{'reset_index': False}),
        #     (['Escuela_ID','CURSO_NORMALIZADO','División'],{'Alumno_ID': 'count'},{'reset_index': False}),
            
        #     (['Nivel_Unificado','CURSO_NORMALIZADO'],{'Alumno_ID':'count'},{'reset_index': False}),
        #     (['Supervisión','CURSO_NORMALIZADO'],{'Alumno_ID':'count'}, {'reset_index': False}),

        # ]
        # generate_group_aggregation_class(group_params_list , os.path.dirname(os.path.abspath(__file__)))
        print('agrupando nominal')
        self.groupby()


    def groupby(self, *args, **kwargs):
        self.df_Escuela_ID_Alumno_ID_count = self.df_Escuela_ID_Alumno_ID_count()
        pass

    def agg(self, *args, **kwargs):
        pass

    def pivot_table(self, *args, **kwargs):
        pass