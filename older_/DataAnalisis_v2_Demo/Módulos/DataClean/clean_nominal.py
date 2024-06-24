import sys
import os
import pandas as pd
# la clave está en pasar los paths en done está la libreria y en donde está la demo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería

def procesar_nominal(dfnom):
    # Asegurarse de que 'Nivel' existe en el DataFrame para evitar errores.
    if 'Nivel' not in dfnom.columns:
        raise ValueError("La columna 'Nivel' no existe en el DataFrame.")

    # Crear la columna 'Nivel_Unificado' directamente sin usar .insert(), por simplicidad y claridad.
    dfnom['Nivel_Unificado'] = dfnom['Nivel']

    # Cambiar los nombres de los niveles en 'Nivel_Unificado'.
    dfnom['Nivel_Unificado'] = dfnom['Nivel_Unificado'].replace({
        'Secundario Orientado': 'Secundario', 
        'Secundario Técnico': 'Secundario'
    })
    [
        listDictFinal , 
        dictValues , 
        Escuelas_IDs
    ] = lib.IO.dataOutput.dataFrameToDict(
        dfnom ,
        [
            'Escuela_ID' ,
            'Nivel',
            'Nivel_Unificado',
            'Gestión',
            'Supervisión',
            'Departamento',
            'Localidad',
            'zona',
            'AMBITO',
            'Regional'
        ],
        'props'
    )

    return listDictFinal , dictValues , Escuelas_IDs

def procesar_nominal_v2(dfnom):
    # Asegurarse de que 'Nivel' existe en el DataFrame para evitar errores.
    if 'Nivel' not in dfnom.columns:
        raise ValueError("La columna 'Nivel' no existe en el DataFrame.")

    # Crear la columna 'Nivel_Unificado' directamente sin usar .insert(), por simplicidad y claridad.
    dfnom['Nivel_Unificado'] = dfnom['Nivel']

    # Cambiar los nombres de los niveles en 'Nivel_Unificado'.
    dfnom['Nivel_Unificado'] = dfnom['Nivel_Unificado'].replace({
        'Secundario Orientado': 'Secundario', 
        'Secundario Técnico': 'Secundario'
    })

    return dfnom