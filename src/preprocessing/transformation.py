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
    print("Transformando datos...crear columna Nivel_Unificado")
    dataframe = crear_columna_nivel(dataframe)
    print("Transformando datos...cambiando nombres de los nivels en la columna Nivel_Unificado")
    dataframe = cambiar_nombres_de_niveles(dataframe)
    # Ejemplo de transformación
    #dataframe['new_column'] = dataframe['Alumno_ID'] * 2 # es un ejemplo..va a multiplicar el alumno id por dos
    return dataframe

def crear_columna_nivel(dataframe: pd.DataFrame) -> pd.DataFrame:
    # genero la columna Nivel_Unificado
    # Asegurarse de que 'Nivel' existe en el DataFrame para evitar errores.
    if 'Nivel' not in dataframe.columns:
        raise ValueError("La columna 'Nivel' no existe en el DataFrame.")
    # Crear la columna 'Nivel_Unificado' directamente sin usar .insert(), por simplicidad y claridad.
    dataframe['Nivel_Unificado'] = dataframe['Nivel']
    return dataframe

def cambiar_nombres_de_niveles(dataframe: pd.DataFrame) -> pd.DataFrame:
    # Cambiar los nombres de los niveles en 'Nivel_Unificado'.
    dataframe['Nivel_Unificado'] = dataframe['Nivel_Unificado'].replace({
        'Secundario Orientado': 'Secundario', 
        'Secundario Técnico': 'Secundario'
    })
    return dataframe

def transformar_y_calcular_porcentaje_desempeño(listaDeColumnas, dF_dataFrameIzquierdo, dF_dataFrameDerecha, ColumnaY, ColumnaX, col_titulo):    
    # Esta función calcula los porcentajes de desempeños de acuerdo a las columnas que se les pasa por parámetros.
    # La idea es que se puedan determinar por escuela, por curso, por división, etc., manteniendo la referencia de Alumno_ID
    # y renombrando las columnas de acuerdo a los parámetros suministrados.    
    # Realizando la fusión de los dataframes.
    dF_desempeño = pd.merge(dF_dataFrameIzquierdo, dF_dataFrameDerecha, how="left", on=listaDeColumnas)    
    # Renombrando las columnas 'Alumno_ID_x' y 'Alumno_ID_y' según los parámetros suministrados, asumiendo que ambas columnas contienen los mismos valores.
    # Esto implica que se puede mantener solo una de estas columnas para evitar duplicados.
    dF_desempeño.rename(columns={'Alumno_ID_x': ColumnaX, 'Alumno_ID_y': ColumnaY}, inplace=True)
    # Calculando el porcentaje de desempeño.
    dF_desempeño[col_titulo] = dF_desempeño[ColumnaY] / dF_desempeño[ColumnaX] * 100    
    # Opcional: Si se desea eliminar una de las columnas de Alumno_ID para evitar redundancia, puedes descomentar la siguiente línea:
    # dF_desempeño.drop(columns=[ColumnaY], inplace=True)
    return dF_desempeño