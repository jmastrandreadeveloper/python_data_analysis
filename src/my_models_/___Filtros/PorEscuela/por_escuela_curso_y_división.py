import pandas as pd

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

def filtrar_matricula_por_escuela_curso_y_division(Escuela_ID ,dFrame,  lista_de_cursos):
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