# acá se agrupan las funciones desetinadas a calcular el desempeño
import json
from functools import reduce
import pandas as pd
import libConfig as lib  # importo las referencias a la librería
import sys
#from io import StringIO
# acá está el config de la librería
sys.path.insert(
    1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs')
# para linux en mi notebook !!
sys.path.insert(
    1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs')


def filtrar_dataframe_avanzado(df, consulta):
    """
    Filtra un DataFrame basado en una consulta expresada como una cadena.
    
    Parámetros:
    - df (pd.DataFrame): El DataFrame a filtrar.
    - consulta (str): La consulta de filtrado, una cadena que expresa la lógica de filtrado
                      con cualquier combinación de condiciones y operadores lógicos.

    Retorna:
    - pd.DataFrame: Un DataFrame filtrado según la consulta dada.
    """
    return df.query(consulta)

def FL_ESCUELA_001_desempeño_y_total_alumnos_por_escuela(unaEscuela,dFrame):
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

#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################

def FL_ESCUELA_002_desempeño_y_total_alumnos_por_curso(unaEscuela, dFrame, lista_de_cursos):    
    # el uso de pivot nos sugiere que el resultado va a ser visualizado como
    # un diagrama de barras
    desempeño_por_curso_df = pd.DataFrame()
    total_alumnos_por_tipo_de_desempeño_por_curso_df = pd.DataFrame()
    rslt_df = dFrame[dFrame['Escuela_ID'] == unaEscuela]        
    if lista_de_cursos:
        rslt_df = rslt_df[rslt_df['CURSO_NORMALIZADO'].isin(lista_de_cursos)]
    #NO USAMOS FILTER DE DATOS DADO QUE EL PIVOTE LO HARÁ POR NOSOSTROS!!
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
    total_alumnos_por_tipo_de_desempeño_por_curso_df = pd.pivot_table(
        rslt_df,
        values='Total_Alumnos_por_Tipo_de_Desempeño',
        index=['DESEMPEÑO'],
        columns=['CURSO_NORMALIZADO'],
        aggfunc='first'
    ).fillna(0)  # Rellenar valores NaN con 0
    total_alumnos_por_tipo_de_desempeño_por_curso_df = total_alumnos_por_tipo_de_desempeño_por_curso_df.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])    
    return desempeño_por_curso_df , total_alumnos_por_tipo_de_desempeño_por_curso_df

#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################

def FL_ESCUELA_003_desempeño_por_curso_division(unaEscuela, dFrame, lista_de_cursos):
    # Inicialización del diccionario para almacenar los resultados.
    dict_desempeño_por_curso_division = {}
    dict_total_alumnos_por_tipo_de_desempeño_por_curso_división = {}
    for CURSO_NORMALIZADO in lista_de_cursos:
        # Filtrado del DataFrame para obtener los datos del curso y la escuela específicos.
        # rslt_df = dFrame[
        #     (dFrame['Escuela_ID'] == unaEscuela) &
        #     (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]

        # Definir una consulta compleja
        #consulta = "(Escuela_ID == 1 & CURSO_NORMALIZADO == 'Matemáticas') | (Calificación >= 90 & CURSO_NORMALIZADO == 'Literatura')"
        consulta = f"(Escuela_ID == {unaEscuela}) & (CURSO_NORMALIZADO == '{CURSO_NORMALIZADO}')"        
        # Filtrar el DataFrame
        
        rslt_df = dFrame.query(consulta)



        # Creación de un DataFrame 'wide' usando pivot_table para organizar los datos por DESEMPEÑO y División.
        # Incluyendo tanto el desempeño como los totales de alumnos.
        desempeño_por_curso_division_df = pd.pivot_table(
            rslt_df,
            index=['DESEMPEÑO'],
            columns='División',
            values='Desempeño_por_Escuela_CURSO_NORMALIZADO_Division',
            aggfunc='first'
        )
        total_alumnos_por_tipo_de_desempeño_por_curso_división_df = pd.pivot_table(
            rslt_df,
            index=['DESEMPEÑO'],
            columns='División',
            values='Total_Alumnos_por_Tipo_de_Desempeño',
            aggfunc='sum'
        )
        # Asegurando el orden correcto de las divisiones y de los niveles de desempeño.
        # Ordenamos las divisiones si es necesario.
        cols = sorted(rslt_df['División'].unique())
        desempeño_por_curso_division_df = desempeño_por_curso_division_df.reindex(columns=cols).fillna(0).reindex(
            ['Crítico',
             'Básico',
             'Medio',
             'Avanzado']
        )
        total_alumnos_por_tipo_de_desempeño_por_curso_división_df = total_alumnos_por_tipo_de_desempeño_por_curso_división_df.reindex(columns=cols).fillna(0).reindex(
            ['Crítico',
             'Básico',
             'Medio',
             'Avanzado']
        )
        # print(unaEscuela)
        # print(CURSO_NORMALIZADO)
        # print(df_wide_desempeno)
        # print('-'*50)
        # Combinación de los DataFrames de desempeño y alumnos en un solo diccionario.
        # combined_dict = {}
        # for desempeno in df_wide_desempeno.index:
        #     combined_dict[desempeno] = {}
        #     for division in cols:
        #         combined_dict[desempeno][division] = {
        #             'Desempeño': df_wide_desempeno.at[desempeno, division],
        #             'Total_Alumnos': df_wide_alumnos.at[desempeno, division]
        #         }
        # # Almacenamiento del diccionario combinado en el diccionario principal.
        # dict_desempeño_por_curso_division[CURSO_NORMALIZADO] = combined_dict
        dict_desempeño_por_curso_division[CURSO_NORMALIZADO] = desempeño_por_curso_division_df
        dict_total_alumnos_por_tipo_de_desempeño_por_curso_división[CURSO_NORMALIZADO] = total_alumnos_por_tipo_de_desempeño_por_curso_división_df
    return dict_desempeño_por_curso_division , dict_total_alumnos_por_tipo_de_desempeño_por_curso_división


# # def consulta_iterativa(Escuela_ID, dFrame, consulta , lista , index_, columns_, values_, aggfunc_ , sorted_ , reindex_) :
# #     dict_desempeño_por_curso_division = {}    
# #     for CURSO_NORMALIZADO in lista:
# #         rslt_df = dFrame.query(consulta)
# #         desempeño_por_curso_division_df = pd.pivot_table(
# #             rslt_df,
# #             index=[index_],
# #             columns=columns_,
# #             values=values_,
# #             aggfunc=aggfunc_
# #         )
# #         cols = sorted(rslt_df[sorted_].unique())
# #         desempeño_por_curso_division_df = desempeño_por_curso_division_df.reindex(columns=cols).fillna(0).reindex(reindex_)
# #         dict_desempeño_por_curso_division[CURSO_NORMALIZADO] = desempeño_por_curso_division_df        
# #     return dict_desempeño_por_curso_division
# def consulta_iterativa(dFrame, Escuela_ID, consulta_base, lista, index_, columns_, values_, aggfunc_, sorted_, reindex_):
#     dict_desempeño_por_curso_division = {}    
#     for CURSO_NORMALIZADO in lista:
#         # Modificar la consulta para cada iteración, incluyendo el curso actual en el bucle
#         consulta_curso = consulta_base.format(Escuela_ID=Escuela_ID, CURSO_NORMALIZADO=CURSO_NORMALIZADO)
#         rslt_df = dFrame.query(consulta_curso)

#         desempeño_por_curso_division_df = pd.pivot_table(
#             rslt_df,
#             index=[index_],
#             columns=columns_,
#             values=values_,
#             aggfunc=aggfunc_
#         )

#         cols = sorted(rslt_df[sorted_].unique())
#         desempeño_por_curso_division_df = desempeño_por_curso_division_df.reindex(columns=cols).fillna(0).reindex(reindex_)
#         dict_desempeño_por_curso_division[CURSO_NORMALIZADO] = desempeño_por_curso_division_df        
#     return dict_desempeño_por_curso_division

# dFrame = pd.DataFrame()

# data = """"Escuela_ID";"CURSO_NORMALIZADO";"División";"Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División";"DESEMPEÑO";"Total_Alumnos_por_Tipo_de_Desempeño";"Desempeño_por_Escuela_CURSO_NORMALIZADO_Division"
# "9";"2°";"A";"31";"Básico";"4";"12.9"
# "9";"2°";"A";"31";"Crítico";"25";"80.65"
# "9";"2°";"A";"31";"Medio";"2";"6.45"
# "9";"2°";"B";"33";"Básico";"5";"15.15"
# "9";"2°";"B";"33";"Crítico";"23";"69.7"
# "9";"2°";"B";"33";"Medio";"5";"15.15"
# "9";"2°";"C";"26";"Básico";"9";"34.62"
# "9";"2°";"C";"26";"Crítico";"15";"57.69"
# "9";"2°";"C";"26";"Medio";"2";"7.69"
# "9";"2°";"D";"28";"Avanzado";"1";"3.57"
# "9";"2°";"D";"28";"Básico";"3";"10.71"
# "9";"2°";"D";"28";"Crítico";"20";"71.43"
# "9";"2°";"D";"28";"Medio";"4";"14.29"
# "9";"3°";"A";"31";"Avanzado";"6";"19.35"
# "9";"3°";"A";"31";"Básico";"13";"41.94"
# "9";"3°";"A";"31";"Crítico";"4";"12.9"
# "9";"3°";"A";"31";"Medio";"8";"25.81"
# "9";"3°";"B";"33";"Avanzado";"4";"12.12"
# "9";"3°";"B";"33";"Básico";"9";"27.27"
# "9";"3°";"B";"33";"Crítico";"16";"48.48"
# "9";"3°";"B";"33";"Medio";"4";"12.12"
# "9";"3°";"C";"27";"Avanzado";"4";"14.81"
# "9";"3°";"C";"27";"Básico";"13";"48.15"
# "9";"3°";"C";"27";"Crítico";"5";"18.52"
# "9";"3°";"C";"27";"Medio";"5";"18.52"
# "9";"3°";"D";"24";"Avanzado";"2";"8.33"
# "9";"3°";"D";"24";"Básico";"8";"33.33"
# "9";"3°";"D";"24";"Crítico";"11";"45.83"
# "9";"3°";"D";"24";"Medio";"3";"12.5"
# "9";"4°";"A";"34";"Avanzado";"3";"8.82"
# "9";"4°";"A";"34";"Básico";"11";"32.35"
# "9";"4°";"A";"34";"Crítico";"13";"38.24"
# "9";"4°";"A";"34";"Medio";"7";"20.59"
# "9";"4°";"B";"32";"Avanzado";"4";"12.5"
# "9";"4°";"B";"32";"Básico";"7";"21.88"
# "9";"4°";"B";"32";"Crítico";"8";"25.0"
# "9";"4°";"B";"32";"Medio";"13";"40.62"
# "9";"4°";"C";"22";"Avanzado";"1";"4.55"
# "9";"4°";"C";"22";"Básico";"8";"36.36"
# "9";"4°";"C";"22";"Crítico";"7";"31.82"
# "9";"4°";"C";"22";"Medio";"6";"27.27"
# "9";"4°";"D";"23";"Avanzado";"3";"13.04"
# "9";"4°";"D";"23";"Básico";"6";"26.09"
# "9";"4°";"D";"23";"Crítico";"9";"39.13"
# "9";"4°";"D";"23";"Medio";"5";"21.74"
# "9";"5°";"A";"30";"Avanzado";"3";"10.0"
# "9";"5°";"A";"30";"Básico";"8";"26.67"
# "9";"5°";"A";"30";"Crítico";"11";"36.67"
# "9";"5°";"A";"30";"Medio";"8";"26.67"
# "9";"5°";"B";"29";"Avanzado";"7";"24.14"
# "9";"5°";"B";"29";"Básico";"8";"27.59"
# "9";"5°";"B";"29";"Crítico";"9";"31.03"
# "9";"5°";"B";"29";"Medio";"5";"17.24"
# "9";"5°";"C";"27";"Avanzado";"2";"7.41"
# "9";"5°";"C";"27";"Básico";"9";"33.33"
# "9";"5°";"C";"27";"Crítico";"11";"40.74"
# "9";"5°";"C";"27";"Medio";"5";"18.52"
# "9";"5°";"D";"31";"Avanzado";"3";"9.68"
# "9";"5°";"D";"31";"Básico";"8";"25.81"
# "9";"5°";"D";"31";"Crítico";"16";"51.61"
# "9";"5°";"D";"31";"Medio";"4";"12.9"
# "9";"6°";"A";"31";"Avanzado";"1";"3.23"
# "9";"6°";"A";"31";"Básico";"13";"41.94"
# "9";"6°";"A";"31";"Crítico";"5";"16.13"
# "9";"6°";"A";"31";"Medio";"12";"38.71"
# "9";"6°";"B";"28";"Avanzado";"2";"7.14"
# "9";"6°";"B";"28";"Básico";"13";"46.43"
# "9";"6°";"B";"28";"Crítico";"4";"14.29"
# "9";"6°";"B";"28";"Medio";"9";"32.14"
# "9";"6°";"C";"29";"Avanzado";"6";"20.69"
# "9";"6°";"C";"29";"Básico";"11";"37.93"
# "9";"6°";"C";"29";"Crítico";"3";"10.34"
# "9";"6°";"C";"29";"Medio";"9";"31.03"
# "9";"6°";"D";"25";"Avanzado";"8";"32.0"
# "9";"6°";"D";"25";"Básico";"4";"16.0"
# "9";"6°";"D";"25";"Crítico";"5";"20.0"
# "9";"6°";"D";"25";"Medio";"8";"32.0"
# "9";"7°";"A";"27";"Avanzado";"3";"11.11"
# "9";"7°";"A";"27";"Básico";"5";"18.52"
# "9";"7°";"A";"27";"Crítico";"4";"14.81"
# "9";"7°";"A";"27";"Medio";"15";"55.56"
# "9";"7°";"B";"25";"Avanzado";"1";"4.0"
# "9";"7°";"B";"25";"Básico";"5";"20.0"
# "9";"7°";"B";"25";"Crítico";"7";"28.0"
# "9";"7°";"B";"25";"Medio";"12";"48.0"
# "9";"7°";"C";"26";"Avanzado";"5";"19.23"
# "9";"7°";"C";"26";"Básico";"4";"15.38"
# "9";"7°";"C";"26";"Crítico";"7";"26.92"
# "9";"7°";"C";"26";"Medio";"10";"38.46"
# "9";"7°";"D";"24";"Avanzado";"2";"8.33"
# "9";"7°";"D";"24";"Básico";"6";"25.0"
# "9";"7°";"D";"24";"Crítico";"7";"29.17"
# "9";"7°";"D";"24";"Medio";"9";"37.5"
# "9";"7°";"E";"28";"Avanzado";"3";"10.71"
# "9";"7°";"E";"28";"Básico";"6";"21.43"
# "9";"7°";"E";"28";"Crítico";"7";"25.0"
# "9";"7°";"E";"28";"Medio";"12";"42.86"""

# # Utilizamos StringIO para convertir la cadena de texto multi-línea en un objeto similar a un archivo.
# # Esto permite a pd.read_csv leer los datos como si vinieran de un archivo CSV.
# dFrame = pd.read_csv(StringIO(data), sep=";")

# lista = ['2°' , '3°' ,'4°' ,'5°' ,'6°' ]
# Escuela_ID = 9
# consulta = f"(Escuela_ID == {Escuela_ID}) & (CURSO_NORMALIZADO == '{lista}')"
# index = 'DESEMPEÑO'
# columns = 'División'
# values = 'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'
# aggfunc = 'first'
# sorted = 'División'
# reindex_ = [
#     'Crítico',
#     'Básico',
#     'Medio',
#     'Avanzado'
# ]
# consulta_iterativa(
#     '9',
#     dFrame,
#     consulta,
#     lista,
#     index,
#     index,
#     columns,
#     values,
#     aggfunc,
#     sorted,
#     reindex_
# )