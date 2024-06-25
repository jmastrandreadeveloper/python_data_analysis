import pandas as pd

from src.preprocessing.grouping.group_by_columns import group_by_column
from src.preprocessing.grouping.aggregate_functions import sum_aggregation
from src.preprocessing.filtering.filter_by_conditions import filter_greater_than
from src.preprocessing.filtering.filter_by_value import filter_by_value

"""
def transform_data: Define una función llamada transform_data.
dataframe: pd.DataFrame: Utiliza anotaciones de tipo 
para indicar que el parámetro dataframe debe ser un objeto de tipo pd.DataFrame (un DataFrame de pandas).
-> pd.DataFrame: Utiliza anotaciones de tipo para indicar 
que la función devuelve un objeto de tipo pd.DataFrame.
"""

def transform_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    # Implementa las funciones de transformación aquí
    print("Transforming data...")
    # Ejemplo de transformación
    dataframe['new_column'] = dataframe['Alumno_ID'] * 2 # es un ejemplo..va a multiplicar el alumno id por dos
    return dataframe
