# acá van las funciones que se usan para calcular las funciones de desempeño
# para las supervisiones
import sys
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería
import pandas       as pd

def FL_SUPERVISIÓN_001_desempeño_por_supervisión(unaSupervisión, dFrame):
    # desempeño por una supervisión en particular
    return

# def FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso(unaSupervisión, dFrame , listaDeCursos):
#     # desempeño para un curso particular de las escuelas de una supervisión en particular
#     # pej todos los 3er años de la supervisión 01 de secundarias orientadas
#     dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso = {}    
#     for CURSO_NORMALIZADO in listaDeCursos:
#         # Filtrado del DataFrame para obtener los datos del curso y la escuela específicos.
#         rslt_df = dFrame[
#             (dFrame['Supervisión'] == unaSupervisión) & 
#             (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]        
#          # Filtrado de las columnas de interés ('DESEMPEÑO', 'Desempeño_por_Escuela_CURSO_NORMALIZADO' y 'Total_Alumnos_por_Tipo_de_Desempeño').
#         new_dataframe = rslt_df.filter(['DESEMPEÑO', 'Desempeño_por_Supervisión_CURSO_NORMALIZADO', 'Total_Alumnos_por_Tipo_de_Desempeño'])        
#         # Renombrado de la columna 'Desempeño_por_Escuela_CURSO_NORMALIZADO' para simplificar.
#         new_dataframe.rename(columns={'Desempeño_por_Supervisión_CURSO_NORMALIZADO': 'Valor'}, inplace=True)        
#         # Establecimiento de 'DESEMPEÑO' como el índice del nuevo DataFrame.
#         new_dataframe.set_index('DESEMPEÑO', inplace=True)        
#         # Reindexación del DataFrame para asegurar el orden de los niveles de desempeño.
#         new_dataframe = new_dataframe.reindex(['Crítico' , 'Básico' , 'Medio' , 'Avanzado'])
#         # Rellenado de valores faltantes en las columnas 'Valor' y 'Total_Alumnos_por_Tipo_de_Desempeño' con 0.
#         new_dataframe['Valor'] = new_dataframe['Valor'].fillna(0)
#         new_dataframe['Total_Alumnos_por_Tipo_de_Desempeño'] = new_dataframe['Total_Alumnos_por_Tipo_de_Desempeño'].fillna(0)        
#         # Conversión de las columnas a diccionarios.
#         desempeno_dict = new_dataframe['Valor'].to_dict()
#         alumnos_dict = new_dataframe['Total_Alumnos_por_Tipo_de_Desempeño'].to_dict()        
#         # Combinación de los diccionarios de desempeño y cantidad de alumnos en un diccionario comprensivo para cada curso.
#         combined_dict = {desempeno: {'Desempeño': desempeno_dict[desempeno], 'Total_Alumnos': alumnos_dict[desempeno]} for desempeno in desempeno_dict}        
#         # Asignación del diccionario combinado al curso correspondiente en el diccionario de resultados.
#         dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso[CURSO_NORMALIZADO] = combined_dict    
#     # Devolución del diccionario con el desempeño y cantidad de alumnos por curso para la escuela especificada.    
#     return dict_FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso

def FL_SUPERVISIÓN_002_desempeño_por_supervisión_curso_(unaSupervisión, dFrame , listaDeCursos):
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
    