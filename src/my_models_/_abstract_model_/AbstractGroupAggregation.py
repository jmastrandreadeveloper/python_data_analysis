from abc import ABC, abstractmethod
import pandas as pd

class AbstractGroupAggregation(ABC):

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe        

    @abstractmethod
    def groupby(self, columns):
        pass

    @abstractmethod
    def agg(self, agg_dict):
        pass

    @abstractmethod
    def pivot_table(self, index, columns, values):
        pass

    #### estos agrupamientos son comunes para ambos dataframes

    
    
    def df_Escuela_ID_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Escuela_ID']):
            result = self.dataframe.groupby(['Escuela_ID']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Escuela_ID', 'CURSO_NORMALIZADO']):
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Escuela_ID', 'CURSO_NORMALIZADO', 'División']):
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'División']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')
        
    def df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Nivel_Unificado', 'CURSO_NORMALIZADO']):
            result = self.dataframe.groupby(['Nivel_Unificado', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')

    def df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count(self):
        if all(col in self.dataframe.columns for col in ['Supervisión', 'CURSO_NORMALIZADO']):
            result = self.dataframe.groupby(['Supervisión', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError('Las columnas especificadas no existen en el dataframe')