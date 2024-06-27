# src/models/abstract_dataframe.py
from abc import ABC, abstractmethod
import pandas as pd

class AbstractDataFrame(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def group_data(self):
        pass

    @abstractmethod
    def filter_data(self):
        pass

    # def agrupar_por_criterio(self,dataframe , listaDeColumnas , agg_dict , reset_index):
    #     # esta función lo que va a hacer es agrupar un dataframe usando diferentes criterios,
    #     # el dFrame no está agrupado, en la lista de columnas están los criterios para agrupar
    #     # el agg_dict es la función matemática que vamos a usar en este caso siempre es count..
    #     # y el reset_index es un boolean que me va a indicar si necesito resetear el índice o no
    #     # esto sirve para cuando tenga que calcular los desempeños con dataframe que ya se han agrupado    
    #     dataframe.reset_index(drop=True, inplace=True)
    #     if reset_index :
    #         dataframe = dataframe.groupby(listaDeColumnas).agg(agg_dict).reset_index()
    #     else:
    #         dataframe = dataframe.groupby(listaDeColumnas).agg(agg_dict)
    #     return dataframe
    def agrupar_por_criterio(self, dataframe, listaDeColumnas, agg_dict, reset_index, columna_resultante):
        """
        Esta función agrupa un DataFrame usando diferentes criterios.
        Parámetros:
        - dataframe: el DataFrame a agrupar.
        - listaDeColumnas: las columnas que definen los criterios de agrupación.
        - agg_dict: diccionario que define las funciones de agregación, por ejemplo {'columna': 'count'}.
        - reset_index: booleano que indica si se debe resetear el índice del DataFrame resultante.
        - columna_resultante: nombre de la columna resultante de la operación de agregación.
        """
        dataframe.reset_index(drop=True, inplace=True)
        
        # Realizar la agrupación y la agregación
        agrupado = dataframe.groupby(listaDeColumnas).agg(agg_dict)
        
        # Renombrar la columna resultante
        agrupado.columns = [columna_resultante if col == list(agg_dict.keys())[0] else col for col in agrupado.columns]
        
        # Resetear el índice si es necesario
        if reset_index:
            agrupado = agrupado.reset_index()
        
        return agrupado