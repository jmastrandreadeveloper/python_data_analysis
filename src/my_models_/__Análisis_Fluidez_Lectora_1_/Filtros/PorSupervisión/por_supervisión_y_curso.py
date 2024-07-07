import pandas as pd

def filtrar_por_supervisión_y_curso(unaSupervisión, dFrame , listaDeCursos):
    # la idea es hacer un dataframe que sea tipo wide, un pivote por desempeño y curso
    # no usar un loop para recorrer los cursos
    # desempeño para un curso particular de las escuelas de una supervisión en particular
    # pej todos los 3er años de la supervisión 01 de secundarias orientadas
    desempeño_por_supervision_curso_wide_df = pd.DataFrame()
    rslt_df = dFrame[(dFrame['Supervisión'] == unaSupervisión)]
          
    if listaDeCursos:
        rslt_df = rslt_df[rslt_df['CURSO_NORMALIZADO'].isin(listaDeCursos)]

    # transponer los datos , pivotear la de desempeño
    desempeño_por_supervision_curso_wide_df = pd.pivot_table(
        rslt_df,
        values='Desempeño_por_Supervisión_CURSO_NORMALIZADO',
        index=['DESEMPEÑO'],
        columns=['CURSO_NORMALIZADO'],
        aggfunc='first'
    ).fillna(0)  # Rellenar valores NaN con 0

    desempeño_por_supervision_curso_wide_df = desempeño_por_supervision_curso_wide_df.reindex(['Crítico', 'Básico', 'Medio', 'Avanzado'])
    
    return desempeño_por_supervision_curso_wide_df