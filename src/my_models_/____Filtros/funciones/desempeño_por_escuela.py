import pandas as pd

def desempeño_por_escuela(unaEscuela , dFrame):
    desempeño_por_escuela_df = pd.DataFrame()
    total_alumnos_por_escuela_df = pd.DataFrame()
    # Filtrado del DataFrame para obtener los datos correspondientes a la escuela dada.
    df = dFrame[dFrame['Escuela_ID'] == unaEscuela]
    # Asumiendo que la estructura de desempeno_df ya es adecuada para el análisis, con las columnas necesarias.
    # Establecer 'DESEMPEÑO' como índice para trabajar con él más fácilmente.
    df.set_index('DESEMPEÑO', inplace=True)
    # Asegurarse de que todos los niveles de desempeño están representados, incluso si no hay datos para algunos.
    df = df.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])
    # Rellenar los valores faltantes en las columnas relevantes para asegurar que todos los niveles de desempeño tienen un valor.
    # AL HACER ESTO NO NECESITO FILTRAR DADO QUE CREO UN NUEVO DATAFRAME CON LA COLUMNA DE INTERÉS
    desempeño_por_escuela_df['Desempeño_por_Escuela'] = df['Desempeño_por_Escuela'].fillna(0)
    total_alumnos_por_escuela_df['Total_Alumnos_por_Tipo_de_Desempeño'] = df['Total_Alumnos_por_Tipo_de_Desempeño'].fillna(0)    
    # # Devolución de dos dataframe con el desempeño y el total de alumnos
    return desempeño_por_escuela_df , total_alumnos_por_escuela_df