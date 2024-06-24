import sys
import os
import pandas as pd
# la clave está en pasar los paths en done está la libreria y en donde está la demo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería

import Módulos.DataETC.desempeño


def procesar_fluidez_lectora_1(df_FluidezLectora_1):
    # Determinar el desempeño por alumno (suponiendo que lib y el método están correctamente definidos e importados).
    df_FluidezLectora_1 = Módulos.DataETC.desempeño.calcular_desempeño_por_alumno(df_FluidezLectora_1)   
    
    # Asegurarse de que 'Nivel' existe en el DataFrame para evitar errores.
    if 'Nivel' not in df_FluidezLectora_1.columns:
        raise ValueError("La columna 'Nivel' no existe en el DataFrame.")

    # Crear la columna 'Nivel_Unificado' directamente sin usar .insert(), por simplicidad y claridad.
    df_FluidezLectora_1['Nivel_Unificado'] = df_FluidezLectora_1['Nivel']

    # # Luego de procesar la columna 'Nivel_Unificado', ajustar el orden para que quede antes de 'separador'
    # # Primero, obtenemos todas las columnas excepto 'Nivel_Unificado' y 'separador'
    # columnas = [col for col in df_FluidezLectora_1.columns if col not in ['Nivel_Unificado', 'separador']]
    
    # # Insertamos 'Nivel_Unificado' antes de 'separador'
    # indice_separador = columnas.index('separador')
    # columnas.insert(indice_separador, 'Nivel_Unificado')   
    

    # Cambiar los nombres de los niveles en 'Nivel_Unificado'.
    df_FluidezLectora_1['Nivel_Unificado'] = df_FluidezLectora_1['Nivel_Unificado'].replace({
        'Secundario Orientado': 'Secundario', 
        'Secundario Técnico': 'Secundario'
    })

    # Reordenar las columnas del DataFrame.
    df_FluidezLectora_1 = df_FluidezLectora_1[[
        'DESEMPEÑO', 'Alumno_ID', 'Operativo', 'CURSO_NORMALIZADO', 'Curso', 'División',
        'Ausente', 'Cantidad_de_palabras', 'Prosodia', 'Incluido', 'Turno', 'Modalidad',
        'Nivel', 'Nivel_Unificado', 'Gestión', 'Supervisión', 'Escuela_ID', 'Departamento',
        'Localidad', 'zona', 'Regional', 'ciclo_lectivo', 'separador'
    ]]
    
    return df_FluidezLectora_1