import pandas as pd

def desempeño_por_escuela_y_curso(unaEscuela, dFrame, lista_de_cursos):    
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