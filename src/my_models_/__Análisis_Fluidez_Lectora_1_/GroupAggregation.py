from src.my_models_._abstract_model_.AbstractGroupAggregation import AbstractGroupAggregation
import pandas as pd
import os
from src.generator_groups import generate_group_aggregation_class

class GroupAggregation(AbstractGroupAggregation):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
        ### 1 -autogenero los grupos para fluidez        
        # group_params_list = [
        #     (['Escuela_ID','DESEMPEÑO'],{'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Escuela_ID','CURSO_NORMALIZADO','DESEMPEÑO'], {'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Escuela_ID','CURSO_NORMALIZADO','División','DESEMPEÑO'],{'Alumno_ID':'count'},{'reset_index': True}),

        #     (['Nivel_Unificado','CURSO_NORMALIZADO','DESEMPEÑO'],{'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Supervisión','CURSO_NORMALIZADO','DESEMPEÑO'],{'Alumno_ID':'count'}, {'reset_index': True}),
        # ]
        # generate_group_aggregation_class(group_params_list , os.path.dirname(os.path.abspath(__file__)))

    def groupby(self, dataframe: pd.DataFrame):
        self.df_alumnos_con_MÁXIMA_cant_palabras = dataframe
        # agrupamientos que salen de la clase abstracta dado que son comunes para los dos dataframes
        self.df_Escuela_ID_Alumno_ID_count_ = self.df_Escuela_ID_Alumno_ID_count()
        self.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count_ = self.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count()
        self.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count_ = self.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count()
        self.df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count_ = self.df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count()
        self.df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count_ = self.df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count()        
        # agrupamiento que son propios de este dataframe de fluidez lectora, estos agruipamientos están
        # en esta función., más abajo , son los que agrupan el desempeño y nos va a servir para poder
        # sacar los pocentajes de desempeño
        self.df_Escuela_ID_DESEMPEÑO_Alumno_ID_count_ = self.df_Escuela_ID_DESEMPEÑO_Alumno_ID_count()        
        self.df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count_ = self.df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count()        
        self.df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count_ = self.df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count()
        self.df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count_ = self.df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count()
        self.df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count_ = self.df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count()

        return

    def agg(self, *args, **kwargs):
        pass

    def pivot_table(self, *args, **kwargs):
        pass    

    def df_Escuela_ID_DESEMPEÑO_Alumno_ID_count(self):
        if all(col in self.df_alumnos_con_MÁXIMA_cant_palabras.columns for col in ['Escuela_ID', 'DESEMPEÑO']):
            result = self.df_alumnos_con_MÁXIMA_cant_palabras.groupby(['Escuela_ID', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')    
    
    def df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count(self):
        if all(col in self.df_alumnos_con_MÁXIMA_cant_palabras.columns for col in ['Escuela_ID', 'CURSO_NORMALIZADO', 'DESEMPEÑO']):
            result = self.df_alumnos_con_MÁXIMA_cant_palabras.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')    

    def df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count(self):
        if all(col in self.df_alumnos_con_MÁXIMA_cant_palabras.columns for col in ['Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'DESEMPEÑO']):
            result = self.df_alumnos_con_MÁXIMA_cant_palabras.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count(self):        
        if all(col in self.df_alumnos_con_MÁXIMA_cant_palabras.columns for col in ['Nivel_Unificado', 'CURSO_NORMALIZADO', 'DESEMPEÑO']):
            result = self.df_alumnos_con_MÁXIMA_cant_palabras.groupby(['Nivel_Unificado', 'CURSO_NORMALIZADO', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count(self):
        if all(col in self.df_alumnos_con_MÁXIMA_cant_palabras.columns for col in ['Supervisión', 'CURSO_NORMALIZADO', 'DESEMPEÑO']):
            result = self.df_alumnos_con_MÁXIMA_cant_palabras.groupby(['Supervisión', 'CURSO_NORMALIZADO', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')