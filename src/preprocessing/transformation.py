import pandas as pd

def transform_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    # Implementa las funciones de transformación aquí
    print("Transforming data...")
    # Ejemplo de transformación
    dataframe['new_column'] = dataframe['Alumno_ID'] * 2 # es un ejemplo..va a multiplicar el alumno id por dos
    return dataframe
