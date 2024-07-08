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
        required_columns = ['Escuela_ID', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Escuela_ID']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count(self):
        required_columns = ['Escuela_ID', 'CURSO_NORMALIZADO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count(self):
        required_columns = ['Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'División']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count(self):
        required_columns = ['Nivel_Unificado', 'CURSO_NORMALIZADO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Nivel_Unificado', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count(self):
        required_columns = ['Supervisión', 'CURSO_NORMALIZADO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Supervisión', 'CURSO_NORMALIZADO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')