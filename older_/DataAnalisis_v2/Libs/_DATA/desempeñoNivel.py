# acá van las funciónes que calculan el desempeño
# de todas las escuelas de la provincia de un nivel determinado
import sys
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería
import pandas       as pd

def FL_NIVEL_001_desempeño_por_nivel(dFrame):
    return

# def FL_NIVEL_002_desempeño_por_nivel_curso(unNivel, dFrame , listaDeCursos):
#     # DADO QUE TENEMOS DEFINIDO EL NIVEL DE LA ESCUELA DENTRO DE LAS PROPIEDADES DE LA ESCUELA
#     # PERO EN EL DATAFRAME DEL AGRUPAMIENTO DEL DESEMPEÑO POR NIVEL Y CURSO LA COLUMNA SE LLAMA Nivel_Unificado
#     if unNivel == 'Secundario Orientado' or unNivel == 'Secundario Técnico' :
#         unNivel = 'Secundario'

#     # desempeño para un curso particular de las escuelas de una supervisión en particular
#     # pej todos los 3er años de la supervisión 01 de secundarias orientadas
#     dict_FL_NIVEL_002_desempeño_por_nivel_curso = {}    
#     for CURSO_NORMALIZADO in listaDeCursos:
#         # Filtrado del DataFrame para obtener los datos del curso y la escuela específicos.
#         rslt_df = dFrame[
#             (dFrame['Nivel_Unificado'] == unNivel) & 
#             (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]        
#          # Filtrado de las columnas de interés ('DESEMPEÑO', 'Desempeño_por_Escuela_CURSO_NORMALIZADO' y 'Total_Alumnos_por_Tipo_de_Desempeño').
#         new_dataframe = rslt_df.filter(['DESEMPEÑO', 'Desempeño_por_Nivel_CURSO_NORMALIZADO', 'Total_Alumnos_por_Tipo_de_Desempeño'])        
#         # Renombrado de la columna 'Desempeño_por_Escuela_CURSO_NORMALIZADO' para simplificar.
#         new_dataframe.rename(columns={'Desempeño_por_Nivel_CURSO_NORMALIZADO': 'Valor'}, inplace=True)        
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
#         dict_FL_NIVEL_002_desempeño_por_nivel_curso[CURSO_NORMALIZADO] = combined_dict    
#     # Devolución del diccionario con el desempeño y cantidad de alumnos por curso para la escuela especificada.    
#     return dict_FL_NIVEL_002_desempeño_por_nivel_curso



def FL_NIVEL_002_desempeño_por_nivel_curso_(unNivel, dFrame , listaDeCursos):

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
    return