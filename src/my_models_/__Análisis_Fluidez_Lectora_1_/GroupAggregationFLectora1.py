import pandas as pd

class GroupAggregationFLectora1:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    def df_Escuela_ID_DESEMPEÑO_Alumno_ID_count(self):
        required_columns = ['Escuela_ID', 'DESEMPEÑO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Escuela_ID', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count(self):
        required_columns = ['Escuela_ID', 'CURSO_NORMALIZADO', 'DESEMPEÑO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count(self):
        required_columns = ['Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'DESEMPEÑO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'División', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count(self):
        required_columns = ['Nivel_Unificado', 'CURSO_NORMALIZADO', 'DESEMPEÑO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Nivel_Unificado', 'CURSO_NORMALIZADO', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')

    def df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count(self):
        required_columns = ['Supervisión', 'CURSO_NORMALIZADO', 'DESEMPEÑO', 'Alumno_ID']
        missing_columns = [col for col in required_columns if col not in self.dataframe.columns]
        if not missing_columns:
            result = self.dataframe.groupby(['Supervisión', 'CURSO_NORMALIZADO', 'DESEMPEÑO']).agg({'Alumno_ID': 'count'})
            return result.reset_index()
        else:
            raise ValueError(f'Las columnas especificadas no existen en el dataframe. Columnas faltantes: {missing_columns}')