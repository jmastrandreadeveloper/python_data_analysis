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

def transform_data_fluidez_lectora(dataframe: pd.DataFrame) -> pd.DataFrame:

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

    def calcular_desempeño_por_alumno(dataframe: pd.DataFrame) -> pd.DataFrame:
            dataframe['DESEMPEÑO'] = dataframe.apply(determinar_desempeño_por_fila, axis=1)
            return dataframe

    def determinar_desempeño_por_fila(row):
        criterios = {
            'Primario': {
                '2°': [(0, 15, 'Crítico'), (16, 45, 'Básico'), (46, 70, 'Medio'), (70, float('inf'), 'Avanzado')],
                '3°': [(0, 30, 'Crítico'), (31, 60, 'Básico'), (61, 90, 'Medio'), (90, float('inf'), 'Avanzado')],
                '4°': [(0, 45, 'Crítico'), (46, 75, 'Básico'), (76, 110, 'Medio'), (110, float('inf'), 'Avanzado')],
                '5°': [(0, 60, 'Crítico'), (61, 90, 'Básico'), (91, 125, 'Medio'), (125, float('inf'), 'Avanzado')],
                '6°': [(0, 75, 'Crítico'), (76, 105, 'Básico'), (106, 140, 'Medio'), (140, float('inf'), 'Avanzado')],
                '7°': [(0, 85, 'Crítico'), (86, 115, 'Básico'), (116, 155, 'Medio'), (155, float('inf'), 'Avanzado')]
            },
            'Secundario Orientado': {
                '1°': [(0, 95, 'Crítico'), (96, 125, 'Básico'), (126, 165, 'Medio'), (165, float('inf'), 'Avanzado')],
                '2°': [(0, 105, 'Crítico'), (106, 135, 'Básico'), (136, 170, 'Medio'), (170, float('inf'), 'Avanzado')],
                '3°': [(0, 115, 'Crítico'), (116, 145, 'Básico'), (146, 175, 'Medio'), (175, float('inf'), 'Avanzado')],
                '4°': [(0, 120, 'Crítico'), (121, 150, 'Básico'), (151, 180, 'Medio'), (180, float('inf'), 'Avanzado')],
                '5°': [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (185, float('inf'), 'Avanzado')],
                '6°': [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (185, float('inf'), 'Avanzado')]
            },
            'Secundario Técnico': {
                '1°': [(0, 95, 'Crítico'), (96, 125, 'Básico'), (126, 165, 'Medio'), (165, float('inf'), 'Avanzado')],
                '2°': [(0, 105, 'Crítico'), (106, 135, 'Básico'), (136, 170, 'Medio'), (170, float('inf'), 'Avanzado')],
                '3°': [(0, 115, 'Crítico'), (116, 145, 'Básico'), (146, 175, 'Medio'), (175, float('inf'), 'Avanzado')],
                '4°': [(0, 120, 'Crítico'), (121, 150, 'Básico'), (151, 180, 'Medio'), (180, float('inf'), 'Avanzado')],
                '5°': [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (185, float('inf'), 'Avanzado')],
                '6°': [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (185, float('inf'), 'Avanzado')]
            }
        }
        curso = row['CURSO_NORMALIZADO']
        nivel = row['Nivel']
        palabras = row['Cantidad_de_palabras']
        
        if nivel in criterios and curso in criterios[nivel]:
            for min_val, max_val, desempeño in criterios[nivel][curso]:
                if min_val <= palabras <= max_val:
                    return desempeño
        return 'Desconocido'  # Caso por defecto si no se encuentra un criterio coincidente

    def reordenar_columnas(dataframe: pd.DataFrame) -> pd.DataFrame:
        columnas_ordenadas = [
            'DESEMPEÑO', 'Alumno_ID', 'Operativo', 'CURSO_NORMALIZADO', 'Curso', 'División', 'Ausente',
            'Cantidad_de_palabras', 'Prosodia', 'Incluido', 'Turno', 'Modalidad', 'Nivel', 'Nivel_Unificado' ,'Gestión',
            'Supervisión', 'Escuela_ID', 'Departamento', 'Localidad', 'zona', 'Regional', 'ciclo_lectivo', 'separador'
        ]
        dataframe = dataframe.reindex(columns=columnas_ordenadas)
        print(dataframe.columns)

        return dataframe
    
    # Implementa las funciones de transformación aquí
    print("Transformando datos...crear columna Nivel_Unificado")
    dataframe = crear_columna_nivel(dataframe)
    print("Transformando datos...cambiando nombres de los nivels en la columna Nivel_Unificado")
    dataframe = cambiar_nombres_de_niveles(dataframe)
    print("Transformando datos...calculando desempeño por alumno")
    dataframe = calcular_desempeño_por_alumno(dataframe)
    print("Transformando datos...reordenando columnas")
    dataframe = reordenar_columnas(dataframe)
    
    return dataframe

def transform_data_nominal(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe

