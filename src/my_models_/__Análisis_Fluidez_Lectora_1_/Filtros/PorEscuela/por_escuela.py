import pandas as pd

def filtrar_datos_institucionales_por_escuela(unaEscuela, dFrame):
    # Inicializa un diccionario vacío para los datos institucionales.
    diccionario_datos_institucionales = {}

    # Filtra el DataFrame para obtener los datos de la escuela especificada.
    df_filtrado = dFrame[dFrame['Escuela_ID'] == unaEscuela]

    # Verifica si se encontraron datos para la escuela especificada.
    if not df_filtrado.empty:
        # Extrae la primera fila de datos como una Serie (asumiendo que hay una única entrada para cada ID de escuela).
        datos_escuela = df_filtrado.iloc[0]

        # Lista de columnas cuyos datos se incluirán en el diccionario.
        columnas_datos = ['Nivel', 'Nivel_Unificado' , 'Gestión', 'Supervisión', 'Departamento', 'Localidad', 'zona', 'AMBITO', 'Regional']

        # Rellena el diccionario con los datos de las columnas especificadas.
        for columna in columnas_datos:
            # Asegura que la columna existe para evitar errores.
            if columna in df_filtrado.columns:
                diccionario_datos_institucionales[columna] = datos_escuela[columna]
            else:
                print(f"La columna '{columna}' no existe en el DataFrame.")

    else:
        print(f"No se encontraron datos para la escuela con ID '{unaEscuela}'.")

    return diccionario_datos_institucionales


def filtrar_por_escuela(unaEscuela,dFrame):
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

def filtrar_matricula_por_escuela(dFrame, Escuela_ID):
    # Filtrar el DataFrame por Escuela_ID
    dFrame_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]
    # Contar Alumno_ID para el DataFrame filtrado
    total_alumnos = dFrame_filtrado['Alumno_ID'].count()
    return total_alumnos

def lista_de_cursos_escuela(dFrame , Escuela_ID):
    # Reset index para poder filtrar por 'Escuela_ID'
    agrupado_reset = dFrame.reset_index()
    # Filtramos por una 'Escuela_ID' específica
    dFrame_filtrado = agrupado_reset[agrupado_reset['Escuela_ID'] == Escuela_ID]
    # busco solamente la columna 'CURSO_NORMALIZADO'
    lista_df = dFrame_filtrado['CURSO_NORMALIZADO']
    # convieto ese df de una columna a una lista
    lista_de_cursos = lista_df.to_list()
    # saco los cursos repetidos
    lista_de_cursos = list(set(lista_de_cursos))
    # y la ordeno
    lista_de_cursos.sort()
    return lista_de_cursos

def listado_de_alumnos(unaEscuela, dFrame , dict):    
    # Filtrar el DataFrame por 'Escuela_ID'
    rslt_df = dFrame[
            (dFrame['Escuela_ID'] == unaEscuela)
    ]
    
    # Eliminar la columna 'separador', si se desea eliminar una columna, se utiliza drop en lugar de pop.
    #rslt_df = rslt_df.drop(columns=['separador'])
    rslt_df = lib.UTILS.utils.eliminar_columna(rslt_df , dict.get('cols_delete') )
    
    # Reordenar las columnas según se especifica
    rslt_df = rslt_df.reindex(columns=dict.get('cols'))
    
    # Convertir el DataFrame a una lista de diccionarios con el formato deseado
    dict_listado_de_alumnos = rslt_df.to_dict(orient=dict.get('orient'))
    
    return dict_listado_de_alumnos