import pandas as pd

def clean_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    # Implementa las funciones de limpieza aquí
    print("Cleaning data...")
    # Ejemplo de limpieza
    dataframe.dropna(inplace=True)
    return dataframe
