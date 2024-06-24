# acá se agrupan las funciones desetinadas a calcular el desempeño
import json
from functools import reduce
import pandas as pd
import libConfig as lib  # importo las referencias a la librería
import sys
# acá está el config de la librería
sys.path.insert(
    1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs')
# para linux en mi notebook !!
sys.path.insert(
    1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs')


# para escuelas en sus diferentes variantes
def FL_ESCUELA_001_desempeño_por_escuela(unaEscuela, dFrame):
    # Filtrado del DataFrame para obtener los datos correspondientes a la escuela dada.
    desempeno_df = dFrame[dFrame['Escuela_ID'] == unaEscuela]
    # Asumiendo que la estructura de desempeno_df ya es adecuada para el análisis, con las columnas necesarias.
    # Establecer 'DESEMPEÑO' como índice para trabajar con él más fácilmente.
    desempeno_df.set_index('DESEMPEÑO', inplace=True)
    # Asegurarse de que todos los niveles de desempeño están representados, incluso si no hay datos para algunos.
    desempeno_df = desempeno_df.reindex(
        ['Crítico', 'Básico', 'Medio', 'Avanzado'])
    # Rellenar los valores faltantes en las columnas relevantes para asegurar que todos los niveles de desempeño tienen un valor.
    desempeno_df['Desempeño_por_Escuela'] = desempeno_df['Desempeño_por_Escuela'].fillna(
        0)
    desempeno_df['Total_Alumnos_por_Tipo_de_Desempeño'] = desempeno_df['Total_Alumnos_por_Tipo_de_Desempeño'].fillna(
        0)
    # Preparar el diccionario de salida que incluirá tanto el desempeño por escuela como la cantidad de alumnos por tipo de desempeño.
    desempeno_dict = {}
    for desempeno in ['Crítico', 'Básico', 'Medio', 'Avanzado']:
        desempeno_dict[desempeno] = {
            'Desempeño': desempeno_df.at[desempeno, 'Desempeño_por_Escuela'],
            'Total_Alumnos': desempeno_df.at[desempeno, 'Total_Alumnos_por_Tipo_de_Desempeño']
        }
    # Devolución del diccionario con el desempeño y cantidad de alumnos por tipo de desempeño para la escuela especificada.
    return desempeno_dict

#### FORMATO PARA CHARTJS ############################################################################################


def FL_ESCUELA_001_desempeño_por_escuela_Pie_ChartJS(unaEscuela, dFrame):
    # Filtrado del DataFrame para obtener los datos correspondientes a la escuela dada.
    desempeno_df = dFrame[dFrame['Escuela_ID'] == unaEscuela]
    # Asumiendo que la estructura de desempeno_df ya es adecuada para el análisis, con las columnas necesarias.
    # Establecer 'DESEMPEÑO' como índice para trabajar con él más fácilmente.
    desempeno_df.set_index('DESEMPEÑO', inplace=True)
    # Asegurarse de que todos los niveles de desempeño están representados, incluso si no hay datos para algunos.
    desempeno_df = desempeno_df.reindex(
        ['Crítico', 'Básico', 'Medio', 'Avanzado'])
    # Rellenar los valores faltantes en las columnas relevantes para asegurar que todos los niveles de desempeño tienen un valor.
    desempeno_df['Desempeño_por_Escuela'] = desempeno_df['Desempeño_por_Escuela'].fillna(
        0)
    desempeno_df['Total_Alumnos_por_Tipo_de_Desempeño'] = desempeno_df['Total_Alumnos_por_Tipo_de_Desempeño'].fillna(
        0)
    # Preparar el diccionario de salida que incluirá tanto el desempeño por escuela como la cantidad de alumnos por tipo de desempeño.
    # desempeno_dict = {}
    # desempeno_dict = {
    #     'datos_pie': {
    #         'labels': ['Crítico', 'Básico', 'Medio', 'Avanzado']
    #     },
    #     'datasets': [
    #         {
    #             'label': "Desempeño por escuela",
    #             'data': [
    #                 desempeno_df.at['Crítico', 'Desempeño_por_Escuela'],
    #                 desempeno_df.at['Básico', 'Desempeño_por_Escuela'],
    #                 desempeno_df.at['Medio', 'Desempeño_por_Escuela'],
    #                 desempeno_df.at['Avanzado', 'Desempeño_por_Escuela']
    #             ]
    #         }
    #     ]
    # }
    # # falta el total_alumnos por desempeño    
    # total_alumnos_dict = {}
    # for desempeno in ['Crítico', 'Básico', 'Medio', 'Avanzado']:
    #     total_alumnos_dict[desempeno] = {
    #         'Total_Alumnos': desempeno_df.at[desempeno, 'Total_Alumnos_por_Tipo_de_Desempeño']
    #     }
    # # Devolución del diccionario con el desempeño y cantidad de alumnos por tipo de desempeño para la escuela especificada.
    return desempeno_df #desempeno_dict , total_alumnos_dict


def FL_ESCUELA_001_desempeño_por_escuela_Pie_ChartJS(unaEscuela, dFrame):
    desempeño_por_escuela_df = pd.DataFrame()
    total_alumnos_por_escuela_df = pd.DataFrame()
    # Filtrado del DataFrame para obtener los datos correspondientes a la escuela dada.
    df = dFrame[dFrame['Escuela_ID'] == unaEscuela]
    # Asumiendo que la estructura de desempeno_df ya es adecuada para el análisis, con las columnas necesarias.
    # Establecer 'DESEMPEÑO' como índice para trabajar con él más fácilmente.
    df.set_index('DESEMPEÑO', inplace=True)
    # Asegurarse de que todos los niveles de desempeño están representados, incluso si no hay datos para algunos.
    df = df.reindex(
        ['Crítico', 'Básico', 'Medio', 'Avanzado'])
    # Rellenar los valores faltantes en las columnas relevantes para asegurar que todos los niveles de desempeño tienen un valor.
    desempeño_por_escuela_df['Desempeño_por_Escuela'] = df['Desempeño_por_Escuela'].fillna(
        0)
    total_alumnos_por_escuela_df['Total_Alumnos_por_Tipo_de_Desempeño'] = df['Total_Alumnos_por_Tipo_de_Desempeño'].fillna(
        0)    
    # # Devolución de dos dataframe con el desempeño y el total de
    return desempeño_por_escuela_df ,  total_alumnos_por_escuela_df
######################################################################################################################


def FL_ESCUELA_002_desempeño_por_curso(unaEscuela, dFrame, listaDeCursos):
    """
    Esta función toma como parámetros una escuela específica, un DataFrame con datos de desempeño,
    y una lista de cursos. Para cada curso en la lista, filtra los datos relevantes del DataFrame,
    ajusta y limpia los datos según sea necesario, y luego convierte los valores de desempeño
    y la cantidad de alumnos por tipo de desempeño para cada nivel ('Crítico', 'Básico', 'Medio', 'Avanzado')
    en un diccionario. Este diccionario se asigna al nombre del curso dentro de un diccionario general que
    acumula esta información para todos los cursos proporcionados.
    Finalmente, la función devuelve este diccionario comprensivo.
    """
    # Inicialización de un diccionario vacío para almacenar los resultados.
    dict_FL_ESCUELA_002_desempeño_por_curso = {}

    # Iteración sobre cada curso en la lista de cursos proporcionada.
    for CURSO_NORMALIZADO in listaDeCursos:
        # Filtrado del DataFrame original para obtener los datos correspondientes a la escuela y curso actual.
        rslt_df = dFrame[
            (dFrame['Escuela_ID'] == unaEscuela) &
            (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]

        # Filtrado de las columnas de interés ('DESEMPEÑO', 'Desempeño_por_Escuela_CURSO_NORMALIZADO' y 'Total_Alumnos_por_Tipo_de_Desempeño').
        new_dataframe = rslt_df.filter(
            ['DESEMPEÑO', 'Desempeño_por_Escuela_CURSO_NORMALIZADO', 'Total_Alumnos_por_Tipo_de_Desempeño'])
        # Renombrado de la columna 'Desempeño_por_Escuela_CURSO_NORMALIZADO' para simplificar.
        new_dataframe.rename(
            columns={'Desempeño_por_Escuela_CURSO_NORMALIZADO': 'Valor'}, inplace=True)
        # Establecimiento de 'DESEMPEÑO' como el índice del nuevo DataFrame.
        new_dataframe.set_index('DESEMPEÑO', inplace=True)
        # Reindexación del DataFrame para asegurar el orden de los niveles de desempeño.
        new_dataframe = new_dataframe.reindex(
            ['Crítico', 'Básico', 'Medio', 'Avanzado'])
        # Rellenado de valores faltantes en las columnas 'Valor' y 'Total_Alumnos_por_Tipo_de_Desempeño' con 0.
        new_dataframe['Valor'] = new_dataframe['Valor'].fillna(0)
        new_dataframe['Total_Alumnos_por_Tipo_de_Desempeño'] = new_dataframe['Total_Alumnos_por_Tipo_de_Desempeño'].fillna(0)
        # Conversión de las columnas a diccionarios.
        desempeno_dict = new_dataframe['Valor'].to_dict()
        alumnos_dict = new_dataframe['Total_Alumnos_por_Tipo_de_Desempeño'].to_dict(
        )
        # Combinación de los diccionarios de desempeño y cantidad de alumnos en un diccionario comprensivo para cada curso.
        combined_dict = {desempeno: {
            'Desempeño': desempeno_dict[desempeno], 'Total_Alumnos': alumnos_dict[desempeno]} for desempeno in desempeno_dict}
        # Asignación del diccionario combinado al curso correspondiente en el diccionario de resultados.
        dict_FL_ESCUELA_002_desempeño_por_curso[CURSO_NORMALIZADO] = combined_dict
    # Devolución del diccionario con el desempeño y cantidad de alumnos por curso para la escuela especificada.
    return dict_FL_ESCUELA_002_desempeño_por_curso

######################################################################################################################


def FL_ESCUELA_002_desempeño_por_curso_Bar_ChartJS(unaEscuela, dFrame, listaDeCursos):    
    desempeño_por_curso_df = pd.DataFrame()
    total_alumnos_por_tipo_de_desempeño_df = pd.DataFrame()
    rslt_df = dFrame[(dFrame['Escuela_ID'] == unaEscuela)]        
    if listaDeCursos:
        rslt_df = rslt_df[rslt_df['CURSO_NORMALIZADO'].isin(listaDeCursos)]
    # transponer los datos , pivotear la de desempeño
    desempeño_por_curso_df = pd.pivot_table(
        rslt_df,
        values='Desempeño_por_Escuela_CURSO_NORMALIZADO',
        index=['DESEMPEÑO'],
        columns=['CURSO_NORMALIZADO'],
        aggfunc='first'
    ).fillna(0)  # Rellenar valores NaN con 0
    desempeño_por_curso_df = desempeño_por_curso_df.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])
    # transponer los datos , pivotear la de desempeño
    total_alumnos_por_tipo_de_desempeño_df = pd.pivot_table(
        rslt_df,
        values='Total_Alumnos_por_Tipo_de_Desempeño',
        index=['DESEMPEÑO'],
        columns=['CURSO_NORMALIZADO'],
        aggfunc='first'
    ).fillna(0)  # Rellenar valores NaN con 0
    total_alumnos_por_tipo_de_desempeño_df = total_alumnos_por_tipo_de_desempeño_df.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])    
    return desempeño_por_curso_df , total_alumnos_por_tipo_de_desempeño_df


def FL_ESCUELA_003_desempeño_por_curso_division(unaEscuela, dFrame, listaDeCursos):
    # Inicialización del diccionario para almacenar los resultados.
    dict_desempeño_por_curso_division = {}
    for CURSO_NORMALIZADO in listaDeCursos:
        # Filtrado del DataFrame para obtener los datos del curso y la escuela específicos.
        rslt_df = dFrame[
            (dFrame['Escuela_ID'] == unaEscuela) &
            (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]
        # Creación de un DataFrame filtrado con las columnas de interés, incluyendo 'Total_Alumnos_por_Tipo_de_Desempeño'.
        new_dataframe = rslt_df.filter(
            ['DESEMPEÑO', 'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division', 'División', 'Total_Alumnos_por_Tipo_de_Desempeño'])
        # Creación de un DataFrame 'wide' usando pivot_table para organizar los datos por DESEMPEÑO y División.
        # Incluyendo tanto el desempeño como los totales de alumnos.
        df_wide_desempeno = pd.pivot_table(
            new_dataframe,
            index=['DESEMPEÑO'],
            columns='División',
            values='Desempeño_por_Escuela_CURSO_NORMALIZADO_Division',
            # Se asume que 'first' es adecuado. Ajustar según necesidad.
            aggfunc='first'
        )
        df_wide_alumnos = pd.pivot_table(
            new_dataframe,
            index=['DESEMPEÑO'],
            columns='División',
            values='Total_Alumnos_por_Tipo_de_Desempeño',
            # Podría ser 'sum' si hay múltiples entradas para el mismo desempeño y división.
            aggfunc='sum'
        )
        # Asegurando el orden correcto de las divisiones y de los niveles de desempeño.
        # Ordenamos las divisiones si es necesario.
        cols = sorted(new_dataframe['División'].unique())
        df_wide_desempeno = df_wide_desempeno.reindex(columns=cols).fillna(
            0).reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])
        df_wide_alumnos = df_wide_alumnos.reindex(columns=cols).fillna(
            0).reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])
        # Combinación de los DataFrames de desempeño y alumnos en un solo diccionario.
        combined_dict = {}
        for desempeno in df_wide_desempeno.index:
            combined_dict[desempeno] = {}
            for division in cols:
                combined_dict[desempeno][division] = {
                    'Desempeño': df_wide_desempeno.at[desempeno, division],
                    'Total_Alumnos': df_wide_alumnos.at[desempeno, division]
                }
        # Almacenamiento del diccionario combinado en el diccionario principal.
        dict_desempeño_por_curso_division[CURSO_NORMALIZADO] = combined_dict
    return dict_desempeño_por_curso_division


def FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel(
        propsEscuela,
        dict_FL_ESCUELA_002_desempeño_por_curso,
        dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso,
        dict_FL_NIVEL_002_desempeño_por_nivel_curso,
        listaDeCursos):
    """
    Esta función hará una combinación de los tres diccionarios que se pasan por parámetros y devolverá
    otro diccionario que va a tener los datos combinados o fusionadas de ellos, estos datos van a servir
    para mostrar las barras verticales donde se va a apreciar la comparación entre un determinado curso 
    y su correspondiente dentro de la supervisión y del nivel al que corresponde la escuela.
    """
    # primer paso : extraer por curso los desempeños de cada uno de los diccionarios:
    # es sabido que la lista de cursos es la clave de los tres diccionarios así que iteramos
    # usando es lista..
    # aramamos un dataframe a partir de ese diccionario, haremos tres dataframe y luego los uniremos
    # de acuerdo al nivel de la escuela, usaremos la palabra grado o año
    # grado para escuelas primarias, año para escuelas secundarias

    dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel = {}

    # Determinar si usar 'Grado' o 'Año' basado en el nivel de la escuela
    gradoAño = 'Grado' if propsEscuela['Nivel'] == 'Primario' else 'Año'

    for CURSO_NORMALIZADO in listaDeCursos:
        # extraigo los valores de desempeño por curso y escuela
        # para ese curso, armo un dataframe donde el desempeño va a estar en una columna
        # Desempeño
        data_escuela_CURSO_NORMALIZADO = [
            [
                'Crítico', dict_FL_ESCUELA_002_desempeño_por_curso[
                    CURSO_NORMALIZADO]['Crítico']['Desempeño']
            ],
            [
                'Básico', dict_FL_ESCUELA_002_desempeño_por_curso[
                    CURSO_NORMALIZADO]['Medio']['Desempeño']
            ],
            [
                'Medio', dict_FL_ESCUELA_002_desempeño_por_curso[CURSO_NORMALIZADO]['Básico']['Desempeño']
            ],
            [
                'Avanzado', dict_FL_ESCUELA_002_desempeño_por_curso[
                    CURSO_NORMALIZADO]['Avanzado']['Desempeño']
            ]
        ]
        # creo un dataframe desempeño
        df_desempeño_data_escuela_CURSO_NORMALIZADO = pd.DataFrame(
            data_escuela_CURSO_NORMALIZADO,
            columns=[
                'Desempeño',
                CURSO_NORMALIZADO
            ]
        )
        # hago lo mismo pero para supervisiones
        # Desempeño
        data_supervisión_CURSO_NORMALIZADO = [
            [
                'Crítico', dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso[
                    CURSO_NORMALIZADO]['Crítico']['Desempeño']
            ],
            [
                'Básico', dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso[
                    CURSO_NORMALIZADO]['Medio']['Desempeño']
            ],
            [
                'Medio', dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso[
                    CURSO_NORMALIZADO]['Básico']['Desempeño']
            ],
            [
                'Avanzado', dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso[
                    CURSO_NORMALIZADO]['Avanzado']['Desempeño']
            ]
        ]

        # renombro la columna curso y le agrego la palabra grado o curso según corresponda
        df_desempeño_data_escuela_CURSO_NORMALIZADO.rename(
            columns={
                CURSO_NORMALIZADO: CURSO_NORMALIZADO + ' ' + gradoAño
            },
            inplace=True
        )
        # creo un dataframe
        df_desempeño_data_supervisión_CURSO_NORMALIZADO = pd.DataFrame(
            data_supervisión_CURSO_NORMALIZADO,
            columns=[
                'Desempeño',
                CURSO_NORMALIZADO + ' ' + gradoAño
            ]
        )
        # debo cambiar el nombre de la columna por el de la supervisión de esa escuela
        df_desempeño_data_supervisión_CURSO_NORMALIZADO.rename(
            columns={
                CURSO_NORMALIZADO + ' ' + gradoAño: 'Sup : ' + propsEscuela['Supervisión'] + ' ' + CURSO_NORMALIZADO + ' ' + gradoAño
            },
            inplace=True
        )
        # hago lo mismo pero para nivel
        # Desempeño
        data_nivel_CURSO_NORMALIZADO = [
            [
                'Crítico', dict_FL_NIVEL_002_desempeño_por_nivel_curso[
                    CURSO_NORMALIZADO]['Crítico']['Desempeño']
            ],
            [
                'Básico', dict_FL_NIVEL_002_desempeño_por_nivel_curso[
                    CURSO_NORMALIZADO]['Medio']['Desempeño']
            ],
            [
                'Medio', dict_FL_NIVEL_002_desempeño_por_nivel_curso[
                    CURSO_NORMALIZADO]['Básico']['Desempeño']
            ],
            [
                'Avanzado', dict_FL_NIVEL_002_desempeño_por_nivel_curso[
                    CURSO_NORMALIZADO]['Avanzado']['Desempeño']
            ]
        ]
        # creo un dataframe
        df_desempeño_data_nivel_CURSO_NORMALIZADO = pd.DataFrame(
            data_nivel_CURSO_NORMALIZADO,
            columns=[
                'Desempeño',
                CURSO_NORMALIZADO + ' ' + gradoAño
            ]
        )
        # debo cambiar el nombre de la columna por el del nivel qué diga el nombre del curso y la palabra nivel
        df_desempeño_data_nivel_CURSO_NORMALIZADO.rename(
            columns={
                CURSO_NORMALIZADO + ' ' + gradoAño: 'Nivel : ' + propsEscuela['Nivel'] + ' ' + CURSO_NORMALIZADO + ' ' + gradoAño
            },
            inplace=True
        )
        # ahora hago la fusión de los tres
        df_desempeño_merged_escuela_supervisión_nivel = reduce(lambda left, right: pd.merge(
            left,
            right,
            on=['Desempeño'],
            how='outer'),
            [
                df_desempeño_data_escuela_CURSO_NORMALIZADO,
                df_desempeño_data_supervisión_CURSO_NORMALIZADO,
                df_desempeño_data_nivel_CURSO_NORMALIZADO
        ]
        )

        df_desempeño_merged_escuela_supervisión_nivel.set_index(
            'Desempeño', inplace=True)
        df_desempeño_merged_escuela_supervisión_nivel.columns.name = 'Entidades'

        combined_dict = {}
        for desempeno in df_desempeño_merged_escuela_supervisión_nivel.index:
            combined_dict[desempeno] = {}
            for entidad in [
                    CURSO_NORMALIZADO + ' ' + gradoAño,
                    'Sup : ' + propsEscuela['Supervisión'] +
                ' ' + CURSO_NORMALIZADO + ' ' + gradoAño,
                    'Nivel : ' + propsEscuela['Nivel'] +
                ' ' + CURSO_NORMALIZADO + ' ' + gradoAño
            ]:
                combined_dict[desempeno][entidad] = {
                    'Desempeño': df_desempeño_merged_escuela_supervisión_nivel.at[desempeno, entidad]
                }
        diccionario_ordenado = {clave: combined_dict[clave] for clave in [
            'Crítico', 'Básico', 'Medio', 'Avanzado',]}
        # Almacenamiento del diccionario combinado en el diccionario principal.
        dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel[
            CURSO_NORMALIZADO] = diccionario_ordenado

    return dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel


# def renombrar_columnas(df, tipo, grado, supervision, nivel):
#     """
#     Renombra las columnas del DataFrame según el tipo (escuela, supervisión, nivel),
#     grado, número de supervisión y nivel educativo.
#     """
#     nuevo_nombre_columnas = {}
#     for columna in df.columns:
#         if "Total_Alumnos" in columna:
#             # Para el caso de escuela
#             if tipo == "escuela":
#                 nuevo_nombre = f"Total_Alumnos_{grado} Grado"
#             # Para el caso de supervisión
#             elif tipo == "supervision":
#                 nuevo_nombre = f"Total_Alumnos_Sup : {supervision} - {nivel} {grado} Grado"
#             # Para el caso de nivel
#             elif tipo == "nivel":
#                 nuevo_nombre = f"Total_Alumnos_Nivel : {nivel} {grado} Grado"
#             nuevo_nombre_columnas[columna] = nuevo_nombre
#         else:
#             nuevo_nombre_columnas[columna] = columna

#     df.rename(columns=nuevo_nombre_columnas, inplace=True)
#     return df

# def FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel__(
#         propsEscuela,
#         dict_FL_ESCUELA_002_desempeño_por_curso,
#         dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso,
#         dict_FL_NIVEL_002_desempeño_por_nivel_curso,
#         listaDeCursos):

#     dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel = {}

#     gradoAño = 'Grado' if propsEscuela['Nivel'] == 'Primario' else 'Año'

#     for CURSO_NORMALIZADO in listaDeCursos:
#         data_sources = [
#             (dict_FL_ESCUELA_002_desempeño_por_curso, CURSO_NORMALIZADO + ' ' + gradoAño),
#             (dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso, 'Sup : ' + propsEscuela['Supervisión'] + ' ' + CURSO_NORMALIZADO + ' ' + gradoAño),
#             (dict_FL_NIVEL_002_desempeño_por_nivel_curso, 'Nivel : ' + propsEscuela['Nivel'] + ' ' + CURSO_NORMALIZADO + ' ' + gradoAño)
#         ]

#         data_frames = []
#         for source, column_name in data_sources:
#             df_temp = pd.DataFrame(source[CURSO_NORMALIZADO]).T.rename(columns={'Desempeño': column_name})
#             df_temp['Desempeño'] = df_temp.index
#             # Aplica la función de renombrar aquí, adaptando los parámetros según sea necesario.
#             # Nota: Ajusta los argumentos de renombrar_columnas según tu caso de uso específico.
#             if 'escuela' in column_name:
#                 df_temp = renombrar_columnas(df_temp, "escuela", CURSO_NORMALIZADO, propsEscuela['Supervisión'], propsEscuela['Nivel'])
#             elif 'Sup :' in column_name:
#                 df_temp = renombrar_columnas(df_temp, "supervision", CURSO_NORMALIZADO, propsEscuela['Supervisión'], propsEscuela['Nivel'])
#             elif 'Nivel :' in column_name:
#                 df_temp = renombrar_columnas(df_temp, "nivel", CURSO_NORMALIZADO, propsEscuela['Supervisión'], propsEscuela['Nivel'])
#             data_frames.append(df_temp)

#         df_merged = reduce(lambda left, right: pd.merge(left, right, on='Desempeño'), data_frames)
#         df_merged.set_index('Desempeño', inplace=True)
#         df_merged.columns.name = 'Entidades'

#         df_merged = df_merged.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])

#         dict_result = df_merged.to_dict(orient='index')

#         dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel[CURSO_NORMALIZADO] = dict_result

#     return dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel

# def FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel(
#     propsEscuela,
#     dict_FL_ESCUELA_002_desempeño_por_curso,
#     dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso,
#     dict_FL_NIVEL_002_desempeño_por_nivel_curso,
#     listaDeCursos):
#     """
#     Mejora de la función para combinar desempeños por curso, supervisión y nivel,
#     retornando un diccionario con los datos fusionados.
#     """

#     dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel = {}

#     # Determinar si usar 'Grado' o 'Año' basado en el nivel de la escuela
#     gradoAño = 'Grado' if propsEscuela['Nivel'] == 'Primario' else 'Año'

#     # Iterar sobre cada curso normalizado en la lista de cursos
#     for CURSO_NORMALIZADO in listaDeCursos:
#         # Preparar datos para cada fuente (escuela, supervisión, nivel)
#         data_sources = [
#             (dict_FL_ESCUELA_002_desempeño_por_curso, CURSO_NORMALIZADO + ' ' + gradoAño),
#             (dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso, 'Sup : ' + propsEscuela['Supervisión'] + ' ' + CURSO_NORMALIZADO + ' ' + gradoAño),
#             (dict_FL_NIVEL_002_desempeño_por_nivel_curso, 'Nivel : ' + propsEscuela['Nivel'] + ' ' + CURSO_NORMALIZADO + ' ' + gradoAño)
#         ]

#         data_frames = []
#         for source, column_name in data_sources:
#             # Convertir el diccionario en DataFrame y renombrar columna
#             df_temp = pd.DataFrame(source[CURSO_NORMALIZADO]).T.rename(columns={'Desempeño': column_name})
#             df_temp['Desempeño'] = df_temp.index
#             data_frames.append(df_temp)

#         # Fusionar DataFrames en uno solo basado en 'Desempeño'
#         df_merged = reduce(lambda left, right: pd.merge(left, right, on='Desempeño'), data_frames)
#         df_merged.set_index('Desempeño', inplace=True)
#         df_merged.columns.name = 'Entidades'

#         # Reordenar filas según el orden específico de desempeño
#         df_merged = df_merged.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])

#         # Convertir el DataFrame fusionado en un diccionario para el resultado final
#         dict_result = df_merged.to_dict(orient='index')

#         # Agregar el diccionario del curso actual al diccionario principal
#         dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel[CURSO_NORMALIZADO] = dict_result

#     return dict_FL_ESCUELA_004_desempeño_por_curso_supervisión_nivel
