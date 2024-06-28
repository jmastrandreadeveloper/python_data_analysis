import pandas as pd

class GroupData:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

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

