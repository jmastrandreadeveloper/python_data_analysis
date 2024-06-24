import sys
import os
import pandas as pd
# la clave está en pasar los paths en done está la libreria y en donde está la demo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería
import DemoPathConfigs as dPC

import Módulos.DataETC.desempeño
import Módulos.GruposYFiltros.Agrupar.agrupar

def agrupar_por_escuela_curso_y_división(df_FluidezLectora_1):
    # DESEMPEÑO POR CURSO Y DIVISIÓN
    # ES UNA TABLA QUE MUESTRA EL DESEMPEÑO POR CADA CURSO Y DIVISIÓN DE LA ESCUELA, ES SIMILAR A LA ANTERIOR
    # PERO EL AGRUPAMIENTO LO HACEMOS AHORA AGREGANDO LA DIVISIÓN
    df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = Módulos.DataETC.desempeño.calcular_desempeño(
        ['Escuela_ID','CURSO_NORMALIZADO','División'],
        Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
            df_FluidezLectora_1,
            ['Escuela_ID','CURSO_NORMALIZADO','División'],
            {'Alumno_ID':'count'},
            True
        ),
        Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
            df_FluidezLectora_1,
            ['Escuela_ID','CURSO_NORMALIZADO','División','DESEMPEÑO'],
            {'Alumno_ID':'count'},
            True
        ),
        'Total_Alumnos_por_Tipo_de_Desempeño',
        'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División',    
        'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'
    )

    #########################################################################################################################
    #########################################################################################################################
    #########################################################################################################################

    # convierto en int la columna Total_Alumnos_por_Tipo_de_Desempeño
    df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
        'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'] = df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'].astype(int).round(0)
    # reducir la cantidad de decimales
    df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
        'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'] = df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'].round(2)
    df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
        'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'] = df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'].fillna(0)
    df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
        'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'] = df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'].fillna(0)
    
    return df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division

# def filtrar_por_escuela_curso_y_division(unaEscuela, dFrame, lista_de_cursos):
#     # Inicialización del diccionario para almacenar los resultados.
#     dict_desempeño_por_curso_division = {}
#     dict_total_alumnos_por_tipo_de_desempeño_por_curso_división = {}
#     for CURSO_NORMALIZADO in lista_de_cursos:
#         # Filtrado del DataFrame para obtener los datos del curso y la escuela específicos.
#         rslt_df = dFrame[
#             (dFrame['Escuela_ID'] == unaEscuela) &
#             (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]
#         # Creación de un DataFrame 'wide' usando pivot_table para organizar los datos por DESEMPEÑO y División.
#         # Incluyendo tanto el desempeño como los totales de alumnos.
#         desempeño_por_curso_division_df = pd.pivot_table(
#             rslt_df,
#             index=['DESEMPEÑO'],
#             columns='División',
#             values='Desempeño_por_Escuela_CURSO_NORMALIZADO_Division',
#             aggfunc='first'
#         )
#         total_alumnos_por_tipo_de_desempeño_por_curso_división_df = pd.pivot_table(
#             rslt_df,
#             index=['DESEMPEÑO'],
#             columns='División',
#             values='Total_Alumnos_por_Tipo_de_Desempeño',
#             aggfunc='sum'
#         )
#         # Asegurando el orden correcto de las divisiones y de los niveles de desempeño.
#         # Ordenamos las divisiones si es necesario.
#         cols = sorted(desempeño_por_curso_division_df['División'].unique())
#         desempeño_por_curso_division_df = desempeño_por_curso_division_df.reindex(columns=cols).fillna(0).reindex(
#             ['Crítico',
#              'Básico',
#              'Medio',
#              'Avanzado']
#         )
#         total_alumnos_por_tipo_de_desempeño_por_curso_división_df = total_alumnos_por_tipo_de_desempeño_por_curso_división_df.reindex(columns=cols).fillna(0).reindex(
#             ['Crítico',
#              'Básico',
#              'Medio',
#              'Avanzado']
#         )
#         dict_desempeño_por_curso_division[CURSO_NORMALIZADO] = desempeño_por_curso_division_df
#         dict_total_alumnos_por_tipo_de_desempeño_por_curso_división[CURSO_NORMALIZADO] = total_alumnos_por_tipo_de_desempeño_por_curso_división_df
#     return dict_desempeño_por_curso_division , dict_total_alumnos_por_tipo_de_desempeño_por_curso_división




def filtrar_por_escuela_curso_y_division(unaEscuela, dFrame, lista_de_cursos):
    dict_desempeño_por_curso_division = {}
    dict_total_alumnos_por_tipo_de_desempeño_por_curso_división = {}
    
    for CURSO_NORMALIZADO in lista_de_cursos:
        rslt_df = dFrame[
            (dFrame['Escuela_ID'] == unaEscuela) &
            (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]
        
        # Aquí asumimos que 'División' ya es una columna en 'dFrame'
        cols = sorted(rslt_df['División'].unique())  # Ordenamos los valores únicos de 'División'
        
        desempeño_por_curso_division_df = pd.pivot_table(
            rslt_df,
            index=['DESEMPEÑO'],
            columns='División',
            values='Desempeño_por_Escuela_CURSO_NORMALIZADO_Division',
            aggfunc='first'
        ).fillna(0)
        
        total_alumnos_por_tipo_de_desempeño_por_curso_división_df = pd.pivot_table(
            rslt_df,
            index=['DESEMPEÑO'],
            columns='División',
            values='Total_Alumnos_por_Tipo_de_Desempeño',
            aggfunc='sum'
        ).fillna(0)
        
        # Reordenamos las columnas según los valores únicos ordenados de 'División'
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
        dict_desempeño_por_curso_division[CURSO_NORMALIZADO] = desempeño_por_curso_division_df
        dict_total_alumnos_por_tipo_de_desempeño_por_curso_división[CURSO_NORMALIZADO] = total_alumnos_por_tipo_de_desempeño_por_curso_división_df
    return dict_desempeño_por_curso_division , dict_total_alumnos_por_tipo_de_desempeño_por_curso_división






# def filtrar_matricula_por_escuela_curso_y_division(dFrame, Escuela_ID , lista_de_cursos):
#     dict_matricula_por_curso_division = {}    
#     agrupado_reset = dFrame.reset_index()
#     for CURSO_NORMALIZADO in lista_de_cursos:
#         # Filtramos por una 'Escuela_ID' específica y un Curso específico
#         dFrame_filtrado = agrupado_reset[
#             (agrupado_reset['Escuela_ID'] == Escuela_ID) &
#             (agrupado_reset['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]        
#         # cambiamos nombres de columnas
#         matricula_por_curso_división_df = dFrame_filtrado.rename(columns={'Alumno_ID': 'Matrícula', 'CURSO_NORMALIZADO' : 'Curso'})
#         # # Pivotamos el DataFrame
#         # df_wide_matricula_curso_división = pd.pivot_table(
#         #     matricula_por_curso_división_df,
#         #     index=['Curso'],
#         #     columns='División',
#         #     values='Matrícula',
#         #     aggfunc='first'
#         # )
#         df_reset = matricula_por_curso_división_df.reset_index()
#         df_matricula_por_curso_división = df_reset['Curso','División','Matrícula']
        
#         dict_matricula_por_curso_division[CURSO_NORMALIZADO] = df_matricula_por_curso_división
#     return dict_matricula_por_curso_division

def filtrar_matricula_por_escuela_curso_y_division(dFrame, Escuela_ID, lista_de_cursos):
    dict_matricula_por_curso_division = {}
    
    # Aseguramos que 'Escuela_ID' sea accesible como columna, reseteando el índice si es necesario
    if 'Escuela_ID' not in dFrame.columns:
        dFrame = dFrame.reset_index()
    
    for CURSO_NORMALIZADO in lista_de_cursos:
        # Filtramos por 'Escuela_ID' específica y un Curso específico
        dFrame_filtrado = dFrame[
            (dFrame['Escuela_ID'] == Escuela_ID) &
            (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)
        ]
        
        # Cambiamos nombres de columnas
        dFrame_filtrado = dFrame_filtrado.rename(columns={'Alumno_ID': 'Matrícula', 'CURSO_NORMALIZADO': 'Curso'})
        df_matricula_por_curso_division = dFrame_filtrado[['Curso', 'División', 'Matrícula']].reset_index(drop=True)
        df_matricula_por_curso_division.set_index('Curso', inplace=True)
        dict_matricula_por_curso_division[CURSO_NORMALIZADO] = df_matricula_por_curso_division       
    
    return dict_matricula_por_curso_division



