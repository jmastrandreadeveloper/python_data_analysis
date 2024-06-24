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

def agrupar_por_nivel_y_curso(df_FluidezLectora_1):
    df_Desempeño_por_Nivel_CURSO_NORMALIZADO = Módulos.DataETC.desempeño.calcular_desempeño(
        ['Nivel_Unificado','CURSO_NORMALIZADO'],
        Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
            df_FluidezLectora_1,
            ['Nivel_Unificado','CURSO_NORMALIZADO'],
            {'Alumno_ID':'count'},
            True
        ),
        Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
            df_FluidezLectora_1,
            ['Nivel_Unificado','CURSO_NORMALIZADO','DESEMPEÑO'],
            {'Alumno_ID':'count'},
            True
        ),
        'Total_Alumnos_por_Tipo_de_Desempeño',
        'Total_Alumnos_por_Nivel_CURSO_NORMALIZADO',    
        'Desempeño_por_Nivel_CURSO_NORMALIZADO'
    )

    #########################################################################################################################
    #########################################################################################################################
    #########################################################################################################################

    df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
        'Total_Alumnos_por_Nivel_CURSO_NORMALIZADO'] = df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
            'Total_Alumnos_por_Nivel_CURSO_NORMALIZADO'].astype(int).round(0)
    df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
        'Total_Alumnos_por_Nivel_CURSO_NORMALIZADO'] = df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
            'Total_Alumnos_por_Nivel_CURSO_NORMALIZADO'].fillna(0)

    df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
        'Total_Alumnos_por_Tipo_de_Desempeño'] = df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
            'Total_Alumnos_por_Tipo_de_Desempeño'].astype(int).round(0)
    df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
        'Total_Alumnos_por_Tipo_de_Desempeño'] = df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
            'Total_Alumnos_por_Tipo_de_Desempeño'].fillna(0)
    
    df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
        'Desempeño_por_Nivel_CURSO_NORMALIZADO'] = df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
            'Desempeño_por_Nivel_CURSO_NORMALIZADO'].round(2)    
    df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
        'Desempeño_por_Nivel_CURSO_NORMALIZADO'] = df_Desempeño_por_Nivel_CURSO_NORMALIZADO[
            'Desempeño_por_Nivel_CURSO_NORMALIZADO'].fillna(0)
    
    return df_Desempeño_por_Nivel_CURSO_NORMALIZADO

def filtrar_por_nivel_y_curso(unNivel, dFrame , listaDeCursos):
    desempeño_por_supervision_curso_wide_df = pd.DataFrame()
    rslt_df = dFrame[(dFrame['Nivel_Unificado'] == unNivel)]
          
    if listaDeCursos:
        rslt_df = rslt_df[rslt_df['CURSO_NORMALIZADO'].isin(listaDeCursos)]

    # transponer los datos , pivotear la de desempeño
    desempeño_por_supervision_curso_wide_df = pd.pivot_table(
        rslt_df,
        values='Desempeño_por_Nivel_CURSO_NORMALIZADO',
        index=['DESEMPEÑO'],
        columns=['CURSO_NORMALIZADO'],
        aggfunc='first'
    ).fillna(0)  # Rellenar valores NaN con 0

    desempeño_por_supervision_curso_wide_df = desempeño_por_supervision_curso_wide_df.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])
    
    return desempeño_por_supervision_curso_wide_df