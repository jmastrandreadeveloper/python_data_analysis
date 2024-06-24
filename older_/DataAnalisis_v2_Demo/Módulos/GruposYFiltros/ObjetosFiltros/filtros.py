# acá obtengo los filtros que se usarán para poder navegar por el informe final
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

def hacer_filtro_por_escuela_curso_y_division(dFrame):
    df_filtro_por_escuela_curso_division = pd.DataFrame()
    # Asegurarse de que el DataFrame tenga solo las columnas necesarias
    df_filtrado = dFrame[['Escuela_ID', 'CURSO_NORMALIZADO', 'División']]
    
    # Agrupar por 'Escuela_ID', 'CURSO_NORMALIZADO' y 'División', y contar las ocurrencias.
    # Aunque en este caso el conteo no es necesario, se hace para usar .reset_index()
    #df_filtro_por_escuela_curso_division = df_filtrado.groupby(['Escuela_ID', 'CURSO_NORMALIZADO', 'División']).size().reset_index(name='Conteo')

    # Nota: El conteo ('Conteo') aquí podría no ser relevante para tu caso, pero se utiliza para permitir el uso de .reset_index()
    # Si solo quieres el listado sin el conteo, puedes omitir el 'size().reset_index(name='Conteo')' y en su lugar usar:
    df_filtro_por_escuela_curso_division = df_filtrado.drop_duplicates()
    #print(df_filtro_por_escuela_curso_division)
    
    return df_filtro_por_escuela_curso_division

def obtener_filtro_por_escuela_curso_y_division(unaEscuela, dFrame, lista_de_cursos):
    # Inicializar el diccionario que almacenará los resultados
    filtro_escuela_curso_division = {}    
    # Filtrar el DataFrame para obtener solo las filas correspondientes a la escuela deseada
    df = dFrame[dFrame['Escuela_ID'] == unaEscuela]
    
    for CURSO_NORMALIZADO in lista_de_cursos:
        # Filtrar el DataFrame para obtener solo las filas que coinciden con el curso actual del bucle
        rslt_df = df[df['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO]
        
        # Obtener la lista de divisiones para el curso actual y almacenarla en el diccionario
        # Utilizamos 'tolist()' para convertir el resultado en una lista
        divisiones = rslt_df['División'].unique().tolist()
        divisiones.sort()  # Ordena la lista de divisiones alfabéticamente
        filtro_escuela_curso_division[CURSO_NORMALIZADO] = divisiones
    return filtro_escuela_curso_division