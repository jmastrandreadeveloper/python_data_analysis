from abc import ABC, abstractmethod
import pandas as pd

class AbstractPreprocessor(ABC):

    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def isnull(self):
        pass

    @abstractmethod
    def notnull(self):
        pass

    @abstractmethod
    def fillna(self, value):
        pass

    @abstractmethod
    def dropna(self):
        pass

    @abstractmethod
    def drop(self, columns, axis):
        pass

    @abstractmethod
    def rename(self, columns):
        pass

    @abstractmethod
    def sort_values(self, by):
        pass

    @abstractmethod
    def sort_index(self):
        pass

    @abstractmethod
    def sort_index(self):
        pass

    def drop_rows(self, column, valores_a_eliminar):
        return self.dataframe.loc[~self.dataframe[column].isin(valores_a_eliminar)]
    
    def drop_rows_multiple_columns(self , columnas, valores_a_eliminar):
        # Crear una máscara booleana que indica las filas a conservar
        mascara = pd.Series([True] * len(self.dataframe))
        for columna in columnas:
            if columna in self.dataframe.columns:
                mascara &= ~self.dataframe[columna].isin(valores_a_eliminar)
        return self.dataframe[mascara]
    
    def conservar_filas(self, columna, valores_a_conservar):
        # Verificar que la columna especificada exista en el DataFrame
        if columna not in self.dataframe.columns:
            raise ValueError(f"La columna '{columna}' no existe en el DataFrame.")
        
        # Verificar que la lista de valores a conservar no esté vacía
        if not valores_a_conservar:
            raise ValueError("La lista de valores a conservar no puede estar vacía.")
        
        # Crear una máscara booleana que indica las filas a conservar
        mascara = self.dataframe[columna].isin(valores_a_conservar)
        
        # Verificar que hay filas que cumplen con la condición
        if not mascara.any():
            raise ValueError("Ninguna fila cumple con los valores especificados para conservar.")
        
        return self.dataframe[mascara]

    def obtener_datos_de_columna(self , nombre_columna, unicos):
        """
        Esta función extrae los datos de una columna específica de un DataFrame,
        los ordena y los devuelve en forma de lista. Opcionalmente, puede devolver
        solo valores únicos.
        
        Parámetros:
        - df (pandas.DataFrame): El DataFrame del cual se extraerán los datos.
        - nombre_columna (str): El nombre de la columna cuyos datos se desean obtener.
        - unicos (bool): Si es True, la función devolverá solo valores únicos.
        
        Retorna:
        - list: Una lista con los datos de la columna especificada, ordenados. Si
        unicos es True, los datos también serán únicos.        """
        
        if nombre_columna in self.dataframe.columns:
            if unicos:
                # Elimina duplicados convirtiendo a set y luego a lista para ordenar
                return sorted(set(self.dataframe[nombre_columna].tolist()))
            else:
                # Simplemente ordena los valores de la columna
                return sorted(self.dataframe[nombre_columna].tolist())
        else:
            # Maneja el caso en que la columna no exista en el DataFrame
            print(f"La columna '{nombre_columna}' no existe en el DataFrame.")
            return []
    
    def reordenar_columnas(self , dataframe , listaDeColumnas):
        # reordenar las columnas
        dataframe = dataframe[listaDeColumnas]
        return dataframe
    
    def filtrar_por_columna(self,columna,condición):
        return self.dataframe[self.dataframe[columna] == condición] 