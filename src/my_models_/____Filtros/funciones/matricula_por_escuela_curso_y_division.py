import pandas as pd

def matricula_por_escuela_curso_y_division(Escuela_ID ,dFrame,  lista_de_cursos):
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