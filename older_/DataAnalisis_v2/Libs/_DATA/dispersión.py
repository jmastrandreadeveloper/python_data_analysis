# acá estarán las funciones de dispersión
import sys
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería
import pandas       as pd

def dispersión(dFrame , listaDeColumnas):
    return

def exp_dispersión_valor_numérico(dataFrame):
     # Mapeo de niveles de desempeño a valores numéricos
    mapeo_desempeño = {
        'Crítico': 1,
        'Básico': 2,
        'Medio': 3,
        'Avanzado': 4
    }

    # Aplicar el mapeo al DataFrame para crear la nueva columna 'NivelNum'
    dataFrame['NivelNum'] = dataFrame['DESEMPEÑO'].map(mapeo_desempeño)

    # Si lo que buscas es calcular una "desviación numérica" basada en la diferencia de cada valor
    # con respecto a un valor de referencia (por ejemplo, la diferencia de cada valor numérico respecto
    # al promedio de estos valores numéricos en el DataFrame), puedes hacerlo de la siguiente manera:
    # Calcular el promedio de los valores numéricos
    promedio = dataFrame['NivelNum'].mean()

    # Este último bloque de código calcula la desviación de cada valor numérico (NivelNum) 
    # respecto al promedio de todos los valores numéricos en NivelNum,
    # y almacena estos valores de desviación en una nueva columna llamada desviacion_numerica.
    # Calcular la desviación de cada valor numérico respecto al promedio
    dataFrame['desviacion_numerica'] = dataFrame['NivelNum'].apply(lambda x: x - promedio)

    return dataFrame , promedio








