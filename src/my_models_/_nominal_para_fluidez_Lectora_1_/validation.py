import pandas as pd
import numpy as np
from src.utils import quitar_retorno_de_columnas

def create_age_reference() -> dict:
    """
    Crear un diccionario de referencia de edades.
    """
    age_reference = {
        ('Primario', '1°'): 6,
        ('Primario', '2°'): 7,
        ('Primario', '3°'): 8,
        ('Primario', '4°'): 9,
        ('Primario', '5°'): 10,
        ('Primario', '6°'): 11,
        ('Primario', '7°'): 12,

        ('Secundario Orientado', '1°'): 13,
        ('Secundario Orientado', '2°'): 14,
        ('Secundario Orientado', '3°'): 15,
        ('Secundario Orientado', '4°'): 16,
        ('Secundario Orientado', '5°'): 17,
        ('Secundario Orientado', '6°'): 18,

        ('Secundario Técnico', '1°'): 13,
        ('Secundario Técnico', '2°'): 14,
        ('Secundario Técnico', '3°'): 15,
        ('Secundario Técnico', '4°'): 16,
        ('Secundario Técnico', '5°'): 17,
        ('Secundario Técnico', '6°'): 18,
    }
    return age_reference

def check_missing_values(dataframe: pd.DataFrame) -> bool:
    """
    Verifica si hay valores faltantes en el DataFrame.
    """
    if dataframe.isnull().sum().sum() > 0:
        print("Validation failed: Missing values found.")
        return False
    return True

def check_column_dtypes(dataframe: pd.DataFrame, expected_dtypes: dict) -> bool:
    """
    Verifica si las columnas tienen los tipos de datos esperados.
    """
    for column, dtype in expected_dtypes.items():
        if column in dataframe.columns and dataframe[column].dtype != dtype:
            print(f"Validation failed: Column '{column}' has incorrect type. Expected {dtype}, got {dataframe[column].dtype}.")
            return False
    return True

def correct_invalid_ages(dataframe: pd.DataFrame, age_reference: dict) -> pd.DataFrame:
    """
    Corrige las edades inválidas utilizando la referencia de edades.
    """
    # def get_correct_age(row):
    #     key = (row['CURSO_NORMALIZADO'], row['Nivel'])
    #     if key in age_reference:
    #         return age_reference[key]
    #     return np.nan  # Return np.nan if key not found

    

    # Definir la función para obtener la edad correcta
    def get_correct_age(row, distancia):
        key = (row['Nivel'], row['Curso'])
        
        if key in age_reference:
            reference_age = age_reference[key]
            try:
                current_age = int(row['Edad'])
                if abs(current_age - reference_age) > distancia:
                    return reference_age
                else:
                    return current_age
            except ValueError:
                # Si la edad no es un número válido, devolver la edad de referencia
                return reference_age
        else:
            try:
                return int(row['Edad'])
            except ValueError:
                # Si la edad no es un número válido y no se encuentra la clave en el diccionario,
                # se devuelve np.nan (o puedes devolver otro valor si lo prefieres)
                return np.nan

    # Convertir edades no válidas a NaN para su corrección
    # dataframe['Edad'] = pd.to_numeric(dataframe['Edad'], errors='coerce')
    # invalid_ages_mask = (dataframe['Edad'] <= 0) | (dataframe['Edad'].isna())
    # print(invalid_ages_mask)

    # esto significa que la diferencia entre la edad leída del df
    # y la que se toma como referencia no debe ser mayor a 2
    # sive para cuando tenemos un valor demasiado grande o muy chico
    # en alguno de esos casos debo poder resolverlo buscando su edad referencia
    distancia_entre_edades = 2

    # Corregir edades inválidas
    # if invalid_ages_mask.any():
    #     dataframe.loc[invalid_ages_mask, 'Edad'] = dataframe[invalid_ages_mask].apply(get_correct_age, axis=1, distancia=distancia_entre_edades)
    
    # Rastrear edades fuera del límite permitido y corregirlas
    # for (curso, nivel), edad in age_reference.items():
    #     mask = (dataframe['CURSO_NORMALIZADO'] == curso) & (dataframe['Nivel'] == nivel)
    #     dataframe.loc[mask & (dataframe['Edad'] > edad), 'Edad'] = edad
    dataframe['Edad_Correcta'] = dataframe.apply(get_correct_age, axis=1, distancia=distancia_entre_edades)
    # reordenar las columnas    
    # Quitar '\r' de los nombres de las columnas
    dataframe = quitar_retorno_de_columnas(dataframe)
    dataframe = dataframe[[
        'ciclo_lectivo',
        'Alumno_ID',
        'Sexo',
        'Edad',
        'Edad_Correcta',
        'CURSO_NORMALIZADO',
        'Curso',
        'División',
        'Turno',
        'Modalidad',
        'Nivel',
        'Gestión',
        'Supervisión',
        'Escuela_ID',
        'Departamento',
        'Localidad',
        'zona',
        'AMBITO',
        'Regional',
    ]]

    #dataframe['Edad'] = dataframe['Edad'].round().astype('Int64')
    return dataframe


def check_invalid_ages(dataframe: pd.DataFrame) -> bool:
    """
    Verifica si hay edades inválidas en el DataFrame.
    """
    if (dataframe['Edad'] <= 0).any() or dataframe['Edad'].isna().any():
        print("Validation failed: Invalid ages found after correction.")
        return False
    return True

def check_duplicates(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Verifica y elimina filas duplicadas en el DataFrame.
    """
    if dataframe.duplicated().sum() > 0:
        print("Validation failed: Duplicate rows found.")
        duplicated_rows = dataframe[dataframe.duplicated()]
        print(duplicated_rows)
        dataframe.drop_duplicates(inplace=True)
        print("Duplicate rows removed.")
    return dataframe

def validate_data(dataframe: pd.DataFrame):
    """
    Función principal de validación de datos.
    """
    print("Validating data...")

    # Create age reference based on the dataframe
    age_reference = create_age_reference()

    # Correct invalid ages
    dataframe = correct_invalid_ages(dataframe, age_reference)
    
    """
    if not check_missing_values(dataframe):
        return False, dataframe

    # Convertir 'Edad' a tipo numérico y asegurarse de que sea int64
    dataframe['Edad'] = pd.to_numeric(dataframe['Edad'], errors='coerce')

    # Example: Check for specific column data types
    expected_dtypes = {        
        'Edad': 'Int64'  # Ensure Edad is integer type
    }

    if not check_column_dtypes(dataframe, expected_dtypes):
        return False, dataframe

    

    # Re-check for invalid ages after correction
    if not check_invalid_ages(dataframe):
        return False, dataframe

    # Check for duplicate rows
    dataframe = check_duplicates(dataframe)
    """

    print("Data validation passed.")
    return True, dataframe

