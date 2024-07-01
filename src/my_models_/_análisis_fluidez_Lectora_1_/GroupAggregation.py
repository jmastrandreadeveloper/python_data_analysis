from src.abstract_model.AbstractGroupAggregation import AbstractGroupAggregation
import pandas as pd
import os
from src.generator_groups import generate_group_aggregation_class

class GroupAggregation(AbstractGroupAggregation):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
        ### 1 -autogenero los grupos
        print('1... generando grupos' )
        group_params_list = [
            (['Escuela_ID', 'CURSO_NORMALIZADO'], {'Alumno_ID': 'count'},{'reset_index': True}),
            (['Escuela_ID','CURSO_NORMALIZADO','División'], {'Alumno_ID': 'count'},{'reset_index': False}),
            (['Nivel','CURSO_NORMALIZADO','División'], {'Alumno_ID': 'count'},{'reset_index': True}),
            (['Escuela_ID', 'CURSO_NORMALIZADO','DESEMPEÑO'], {'Alumno_ID': 'count'},{'reset_index': True}),
        ]
        generate_group_aggregation_class(group_params_list , os.path.dirname(os.path.abspath(__file__)))

    def groupby(self, *args, **kwargs):
        ### 2 -importar la clase para poder usar los métodos de agrupamientos
        print('2... accediendo a los grupos' )
        # incluir la clase en el archivo __init__.py de esta carpeta
        self.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count()
        self.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count()
        self.df_Nivel_CURSO_NORMALIZADO_División_Alumno_ID_count = self.df_Nivel_CURSO_NORMALIZADO_División_Alumno_ID_count()
        self.df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count()

        return

    def agg(self, *args, **kwargs):
        pass

    def pivot_table(self, *args, **kwargs):
        pass

    def agrupar_a(self , columnas , func):
        # acá le mandamos las columnas para que se sepa qué vamos a agrupar
        return
    def df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Escuela_ID', 'CURSO_NORMALIZADO']):
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Escuela_ID', 'CURSO_NORMALIZADO', 'División']):
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'División']).agg({'Alumno_ID': 'count'})
            return result
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Nivel_CURSO_NORMALIZADO_División_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Nivel', 'CURSO_NORMALIZADO', 'División']):
            result = self.dataframe.groupby(['Nivel', 'CURSO_NORMALIZADO', 'División']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Escuela_ID', 'CURSO_NORMALIZADO', 'DESEMPEÑO']):
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

