import sys
import pandas as pd
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería
#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

# acá voy a agrupar las diferentes maneras de otener matrículas de una institución educativa
def matricula_por_escuela(dFrame, Escuela_ID):
    # Filtrar el DataFrame por Escuela_ID
    dFrame_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]
    # Contar Alumno_ID para el DataFrame filtrado
    total_alumnos = dFrame_filtrado['Alumno_ID'].count()
    return total_alumnos

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

# def matricula_por_curso_no_agrupado(dFrame, Escuela_ID):
#     """
#     se envía el dataframe se hace un filtro y luego se hace un agrupamiento específico por Escuela_ID
#     """
#     # Filtrar el DataFrame por Escuela_ID
#     dFrame_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]
#     # Agrupar por CURSO_NORMALIZADO y contar Alumno_ID para cada grupo
#     #agrupado = dFrame_filtrado.groupby('CURSO_NORMALIZADO').agg({'Alumno_ID': 'count'})
#     agrupado = lib.agrupar.agrupar_por_criterio(
#         dFrame_filtrado,
#         ['CURSO_NORMALIZADO'],
#         {'Alumno_ID': 'count'},
#         False
#     )
#     # Convertir el resultado agrupado en un diccionario
#     # No es necesario usar unstack aquí
#     diccionarioMatriculaPorCurso = agrupado.to_dict()['Alumno_ID']
#     return diccionarioMatriculaPorCurso

# def matricula_por_curso_agrupado(dFrameAgrupado , Escuela_ID):
#     """
#     la diferencia con el metodo de arriba es que el agrupado se hace una sola vez
#     y luego se hace el filtrado
#     """    
#     # Reset index para poder filtrar por 'Escuela_ID'
#     agrupado_reset = dFrameAgrupado.reset_index()
#     # Filtramos por una 'Escuela_ID' específica
#     dFrame_filtrado = agrupado_reset[agrupado_reset['Escuela_ID'] == Escuela_ID]
#     # Creamos un diccionario con los cursos como llaves y el total de alumnos como valores
#     diccionarioMatriculaPorCurso = dFrame_filtrado.set_index('CURSO_NORMALIZADO')['Alumno_ID'].to_dict()
#     return diccionarioMatriculaPorCurso


def matricula_por_curso(dFrame , Escuela_ID):
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

#########################################################################################################################
#########################################################################################################################
#########################################################################################################################

# def matricula_por_curso_division_no_agrupado(dFrame, Escuela_ID):
#     # Filtrar el DataFrame por Escuela_ID
#     dFrame_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]
#     # Agrupar por CURSO_NORMALIZADO y División, y contar Alumno_ID para cada grupo
#     # agrupado = dFrame_filtrado.groupby(['CURSO_NORMALIZADO', 'División']).agg({'Alumno_ID': 'count'})
#     agrupado = lib.agrupar.agrupar_por_criterio(
#         dFrame_filtrado,
#         ['CURSO_NORMALIZADO', 'División'],
#         {'Alumno_ID': 'count'},
#         False
#     )
#     # Convertir el resultado en un diccionario anidado
#     diccionarioCursosYDivisiones = agrupado['Alumno_ID'].unstack(fill_value=0).to_dict(orient='index')
#     return diccionarioCursosYDivisiones

# chequear esto si funciona correctamente..!!!!
# def matricula_por_curso_division_no_agrupado_v2(dFrame, Escuela_ID):
#     # Filtrar el DataFrame por Escuela_ID
#     dFrame_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]
#     # Agrupar por CURSO_NORMALIZADO y División, y contar Alumno_ID para cada grupo
#     # agrupado = dFrame_filtrado.groupby(['CURSO_NORMALIZADO', 'División']).agg({'Alumno_ID': 'count'})
#     agrupado = lib.agrupar.agrupar_por_criterio(
#         dFrame_filtrado,
#         ['CURSO_NORMALIZADO', 'División'],
#         {'Alumno_ID': 'count'},
#         False
#     )
#     # Convertir el resultado en un diccionario anidado
#     diccionarioCursosYDivisiones = agrupado['Alumno_ID'].unstack(fill_value=0).to_dict(orient='index')    
#     # Eliminar las divisiones con conteo cero en cada curso
#     for curso, divisiones in list(diccionarioCursosYDivisiones.items()):  # Usamos list() para evitar RuntimeError
#         # Creamos una lista de las divisiones a eliminar para este curso
#         divisiones_a_eliminar = [division for division, conteo in divisiones.items() if conteo == 0]
#         # Eliminamos las divisiones con conteo cero
#         for division in divisiones_a_eliminar:
#             del diccionarioCursosYDivisiones[curso][division]    
#     return diccionarioCursosYDivisiones 


# def matricula_por_curso_division_agrupado(dFrameAgrupado, Escuela_ID):
#     # En este código, la comprensión de diccionario interna 
#     # {division: alumnos for division, alumnos in divisiones.items() if alumnos != 0} 
#     # crea un nuevo diccionario para cada curso, incluyendo solo aquellas divisiones 
#     # cuyos valores de alumnos no son cero. 
#     # Esto se hace para cada curso en el DataFrame pivotado al iterar sobre .to_dict(orient='index').items(), 
#     # lo que garantiza que solo los pares clave-valor (división-alumnos) 
#     # con un número de alumnos diferente de cero se incluyan en el diccionario final diccionarioCursosYDivisiones.
#     # Reset index para poder filtrar por 'Escuela_ID'
#     agrupado_reset = dFrameAgrupado.reset_index()
#     # Filtramos por una 'Escuela_ID' específica
#     dFrame_filtrado = agrupado_reset[agrupado_reset['Escuela_ID'] == Escuela_ID]
#     # Pivotamos el DataFrame
#     pivotado = dFrame_filtrado.pivot(index='CURSO_NORMALIZADO', columns='División', values='Alumno_ID').fillna(0).astype(int)    
#     # Creamos el diccionario de cursos y divisiones, omitiendo los valores cero
#     diccionarioCursosYDivisiones = {
#         curso: {division: alumnos for division, alumnos in divisiones.items() if alumnos != 0}
#         for curso, divisiones in pivotado.to_dict(orient='index').items()
#     }    
#     return diccionarioCursosYDivisiones

def matricula_por_curso_division(dFrame, Escuela_ID , lista_de_cursos):
    dict_matricula_por_curso_division = {}    
    agrupado_reset = dFrame.reset_index()
    for CURSO_NORMALIZADO in lista_de_cursos:
        # Filtramos por una 'Escuela_ID' específica y un Curso específico
        dFrame_filtrado = agrupado_reset[
            (agrupado_reset['Escuela_ID'] == Escuela_ID) &
            (agrupado_reset['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]        
        # cambiamos nombres de columnas
        matricula_por_curso_división_df = dFrame_filtrado.rename(columns={'Alumno_ID': 'Matrícula', 'CURSO_NORMALIZADO' : 'Curso'})
        # Pivotamos el DataFrame
        df_wide_matricula_curso_división = pd.pivot_table(
            matricula_por_curso_división_df,
            index=['Curso'],
            columns='División',
            values='Matrícula',
            aggfunc='first'
        )
        dict_matricula_por_curso_division[CURSO_NORMALIZADO] = df_wide_matricula_curso_división
    return dict_matricula_por_curso_division


#########################################################################################################################
#########################################################################################################################
#########################################################################################################################