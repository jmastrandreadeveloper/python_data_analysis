from src.my_models_._abstract_model_.AbstractPreprocessor import AbstractPreprocessor
import pandas as pd

class Preprocessor(AbstractPreprocessor):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def isnull(self, *args, **kwargs):
        pass

    def notnull(self, *args, **kwargs):
        pass

    def fillna(self, *args, **kwargs):
        pass

    def dropna(self, *args, **kwargs):
        pass

    def drop(self, *args, **kwargs):
        pass

    def rename(self, *args, **kwargs):
        pass

    def sort_values(self, *args, **kwargs):
        pass

    def sort_index(self, *args, **kwargs):
        pass

    def clean_dataframe(self , dataframe, int_columns, float_columns):
        for col in int_columns:
            dataframe[col] = dataframe[col].astype(int).round(0).fillna(0)
        for col in float_columns:
            dataframe[col] = dataframe[col].round(2).fillna(0)
            
        return dataframe
    
    def get_alumnos_incluidos_SI(self,dataframe):
        return dataframe[dataframe['Incluido'] == 'Si']

    def get_alumnos_incluidos_NO(self,dataframe):
        return dataframe[dataframe['Incluido'] == 'No']

    def get_alumnos_con_DESEMPEÑO(self,dataframe):
        return dataframe[dataframe['DESEMPEÑO'] != '-']
    
    def get_alumnos_sin_DESEMPEÑO(self,dataframe):
        return dataframe[dataframe['DESEMPEÑO'] == '-']
    
    def get_alumnos_con_más_de_300_palabras(self,dataframe):
        # Hacer una copia del DataFrame original para evitar SettingWithCopyWarning
        dataframe = dataframe.copy()
        # Convertir los valores de 'Cantidad_de_palabras' a números, reemplazando los no numéricos con NaN
        dataframe['Cantidad_de_palabras'] = pd.to_numeric(dataframe['Cantidad_de_palabras'], errors='coerce')
        
        # Crear DataFrames separados para valores menores y mayores o iguales a 300
        return dataframe[dataframe['Cantidad_de_palabras'] >= 300].copy()
    
    def get_alumnos_con_menos_de_300_palabras(self,dataframe):
        # Hacer una copia del DataFrame original para evitar SettingWithCopyWarning
        dataframe = dataframe.copy()
        # Convertir los valores de 'Cantidad_de_palabras' a números, reemplazando los no numéricos con NaN
        dataframe['Cantidad_de_palabras'] = pd.to_numeric(dataframe['Cantidad_de_palabras'], errors='coerce')
        
        # Crear DataFrames separados para valores menores y mayores o iguales a 300
        return dataframe[dataframe['Cantidad_de_palabras'] < 300].copy()   

    def get_mejor_medición_por_alumno(self,dataframe,):        
        def convert_to_int_or_str(value):
            try:
                return int(value)
            except (ValueError, TypeError):
                return '-'
        #############################################################################################################    
        df_new = dataframe.sort_values('Cantidad_de_palabras', ascending=False).drop_duplicates(['Alumno_ID']).sort_index()

        for col in ['Cantidad_de_palabras', 'Prosodia']:
            df_new[col] = pd.to_numeric(df_new[col], errors='coerce').fillna('-').apply(convert_to_int_or_str)

        df_filtered = df_new[df_new['Cantidad_de_palabras'].apply(lambda x: isinstance(x, int) and x < 300 or x == '-')]
        df_mejores_mediciones = df_filtered.sort_values(by='Cantidad_de_palabras', ascending=False).drop_duplicates(subset=['Alumno_ID'])

        return df_mejores_mediciones
    
    def filtrar_dataframe(self,dataframe):        
        # filtrar el dataframe para su análisis
        # alumnos incluidos = Si
        self._df_alumnos_incluidos_SI = self.get_alumnos_incluidos_SI(dataframe)
        # alumnos incluidos = No
        self._df_alumnos_incluidos_NO = self.get_alumnos_incluidos_NO(dataframe)
        # alumnos con DESEMPEÑO
        self._df_alumnos_con_DESEMPEÑO = self.get_alumnos_con_DESEMPEÑO(self._df_alumnos_incluidos_NO)
        # alumnos sin DESEMPEÑO
        self._df_alumnos_sin_DESEMPEÑO = self.get_alumnos_sin_DESEMPEÑO(self._df_alumnos_incluidos_NO)
        # alumnos con < de 300 palabras leídas
        self._df_alumnos_menor_a_300_palabras = self.get_alumnos_con_menos_de_300_palabras(self._df_alumnos_con_DESEMPEÑO)
        # alumnos con > de 300 palabras leídas
        self._df_alumnos_mayor_a_300_palabras = self.get_alumnos_con_más_de_300_palabras(self._df_alumnos_con_DESEMPEÑO)
        # alumnos con mázxima cantidad de palabras leídas
        self._df_alumnos_con_MÁXIMA_cant_palabras = self.get_mejor_medición_por_alumno(self._df_alumnos_menor_a_300_palabras)

        return