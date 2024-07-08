import sys
import os
import pandas as pd

def filtrar_por_escuela_y_curso(unaEscuela, dFrame, lista_de_cursos):    
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

def filtrar_matricula_por_escuela_y_curso(Escuela_ID , dFrame , ):
    """
    la diferencia con el metodo de arriba es que el agrupado se hace una sola vez
    y luego se hace el filtrado
    """    
    # Reset index para poder filtrar por 'Escuela_ID'
    agrupado_reset = dFrame.reset_index()
    # Filtramos por una 'Escuela_ID' específica
    dFrame_filtrado = agrupado_reset[agrupado_reset['Escuela_ID'] == Escuela_ID]
    # filtramos las columnas que necesitamos
    dFrame_filtrado = dFrame_filtrado.filter(['CURSO_NORMALIZADO', 'Alumno_ID'])
    # cambiar el nombre de la columna Alumno_ID 'por Matrícula'
    matricula_por_curso_df = dFrame_filtrado.rename(columns={'Alumno_ID': 'Matrícula', 'CURSO_NORMALIZADO' : 'Curso'})
    # set_index por 'CURSO_NORMALIZADO'
    matricula_por_curso_df.set_index('Curso', inplace=True)
    # Creamos un diccionario con los cursos como llaves y el total de alumnos como valores
    #diccionarioMatriculaPorCurso = dFrame_filtrado.set_index('CURSO_NORMALIZADO')['Alumno_ID'].to_dict()
    return matricula_por_curso_df