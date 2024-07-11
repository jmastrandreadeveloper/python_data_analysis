import pandas as pd

def matricula_por_escuela_y_curso(Escuela_ID , dFrame , ):
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