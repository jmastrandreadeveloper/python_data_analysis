# acá se agrupan las funciones desetinadas a calcular la dispersión
import json
from functools import reduce
import pandas as pd
import libConfig as lib  # importo las referencias a la librería
import sys
# acá está el config de la librería
sys.path.insert(
    1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs')
# para linux en mi notebook !!
sys.path.insert(
    1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs')


def FL_ESCUELA_001_dispersión_por_curso_division(unaEscuela, dFrame, lista_de_cursos):
    # hacemos el filtrado por cada escuela
    for CURSO_NORMALIZADO in lista_de_cursos:
        # Filtrado del DataFrame para obtener los datos del curso y la escuela específicos.
        rslt_df = dFrame[
            (dFrame['Escuela_ID'] == unaEscuela) &
            (dFrame['CURSO_NORMALIZADO'] == CURSO_NORMALIZADO)]
        
        print(rslt_df)

    return