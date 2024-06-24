import sys
import os
import pandas as pd
# la clave está en pasar los paths en done está la libreria y en donde está la demo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería

# leer paths específico de la demo, por ejemplo las rutas de los archivos
import DemoPathConfigs as dPC # esto es para configurar los path internos al proyecto
# los módulos nos ayudan a hacer cosas que no son parte de la librería
# pero hay ocasiones que sí van a usar cosas de la librería
#import Módulos.ProcessData
#import RepPython.DataAnalisis_v2_Demo.Módulos.NO_GroupData
#import Módulos.CalcularDesempeño
import Módulos.Helpers.Helper as ayuda


import Módulos.DataClean.clean_nominal
import Módulos.DataClean.clean_fluidez_lectora

import Módulos.GruposYFiltros.Agrupar.agrupar

import Módulos.GruposYFiltros.PorEscuela.por_escuela
import Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso
import Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división

import Módulos.GruposYFiltros.PorSupervisión.por_supervisión_y_curso
import Módulos.GruposYFiltros.PorNivel.por_nivel_y_curso


##################################################################################################################################
# CARPETA BASE DEL PROYECTO DEMO
carpeta         = os.path.dirname(__file__) # me trae toda la ruta completa en donde está el proyecto, no la librería!
##################################################################################################################################



# DEFINICIÓN DE LOS NOMBRES DE LOS DATA FRAMES QUE SE VAN A USAR :
# data frame nominal
dfnom = pd.DataFrame()
# data frame fluidez lectora 1
df_FluidezLectora_1 = pd.DataFrame()

dfnom = lib.IO.dataFetching.fetchCSV(
    dPC.carpetaDemo + r'/BasesDeEntrada/Nominal.csv'
)
df_FluidezLectora_1 = lib.IO.dataFetching.fetchCSV(
    dPC.carpetaDemo + r'/BasesDeEntrada/Fluidez Lectora 1.csv'
)

# lista de todos los Escuela_Ids
lista_Escuela_IDs = lib.UTILS.utils.obtener_datos_de_columna(
    dfnom, 
    'Escuela_ID',
    True
)



[listDictFinal , 
 dictValues , 
 Escuelas_IDs] = Módulos.DataClean.clean_nominal.procesar_nominal(dfnom)
df_FluidezLectora_1 = Módulos.DataClean.clean_fluidez_lectora.procesar_fluidez_lectora_1(df_FluidezLectora_1)
# lib.IO.dataOutput.dataFrameToCSV(
#     carpeta + r'/BasesDeSalida/FluidezLectora1procesado',
#     df_FluidezLectora_1
# )

mat_Escuela_ID_Curso = Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
    dfnom,
    [
        'Escuela_ID', 'CURSO_NORMALIZADO'    
    ],
    {'Alumno_ID': 'count'},
    False
)

mat_Escuela_ID_Curso_División = Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
    dfnom,
    [
        'Escuela_ID','CURSO_NORMALIZADO','División'
    ],
    {'Alumno_ID': 'count'},
    False
)

FL_1_mat_Escuela_ID_Curso = Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
    df_FluidezLectora_1,
    [
        'Escuela_ID', 'CURSO_NORMALIZADO'    
    ],
    {'Alumno_ID': 'count'},
    False
)

FL_1_mat_Escuela_ID_Curso_División = Módulos.GruposYFiltros.Agrupar.agrupar.agrupar_por_criterio(
    df_FluidezLectora_1,
    [
        'Escuela_ID','CURSO_NORMALIZADO','División'
    ],
    {'Alumno_ID': 'count'},
    False
)

# df_FL_1_dispersión_por_grupo= Módulos.GroupData.agrupar_dispersión_fluidez_lectora_con_alumnos_y_tamaño(df_FluidezLectora_1)
# # lib.IO.dataOutput.dataFrameToCSV(
# #     carpeta + r'/BasesDeSalida/df_FL_1_dispersión_por_grupo',
# #     df_FL_1_dispersión_por_grupo
# # )

# df_FL_1_dispersión_individual= Módulos.GroupData.agrupar_dispersión_analisis_individual(df_FluidezLectora_1)
# # lib.IO.dataOutput.dataFrameToCSV(
# #     carpeta + r'/BasesDeSalida/df_FL_1_dispersión_individual',
# #     df_FL_1_dispersión_individual
# # )

df_Desempeño_por_Escuela = Módulos.GruposYFiltros.PorEscuela.por_escuela.agrupar_por_escuela(
    df_FluidezLectora_1
)
# lib.IO.dataOutput.dataFrameToCSV(
#     carpeta + r'/BasesDeSalida/df_Desempeño_por_Escuela',
#     df_Desempeño_por_Escuela
# )

df_Desempeño_por_Escuela_CURSO_NORMALIZADO = Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso.agrupar_por_escuela_y_curso(
    df_FluidezLectora_1
)
# lib.IO.dataOutput.dataFrameToCSV(
#     carpeta + r'/BasesDeSalida/df_Desempeño_por_Escuela_CURSO_NORMALIZADO',
#     df_Desempeño_por_Escuela_CURSO_NORMALIZADO,
# )

df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división.agrupar_por_escuela_curso_y_división(
    df_FluidezLectora_1
)
# lib.IO.dataOutput.dataFrameToCSV(
#     carpeta + r'/BasesDeSalida/df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division',
#     df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division
# )

df_Desempeño_por_Supervisión_CURSO_NORMALIZADO = Módulos.GruposYFiltros.PorSupervisión.por_supervisión_y_curso.agrupar_por_supervisión_y_curso(
    df_FluidezLectora_1
)
# lib.IO.dataOutput.dataFrameToCSV(
#     carpeta + r'/BasesDeSalida/df_Desempeño_por_Supervisión_CURSO_NORMALIZADO',
#     df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,
# )

df_Desempeño_por_Nivel_CURSO_NORMALIZADO = Módulos.GruposYFiltros.PorNivel.por_nivel_y_curso.agrupar_por_nivel_y_curso(
    df_FluidezLectora_1
)
# lib.IO.dataOutput.dataFrameToCSV(
#     carpeta + r'/BasesDeSalida/df_Desempeño_por_Nivel_CURSO_NORMALIZADO',
#     df_Desempeño_por_Nivel_CURSO_NORMALIZADO
# )

# USO LA CLASE DE AYUDA, LA CREO POR FUERA, NO NECESITO CREARLA DENTRO DEL BUCLE
# POR PARÁMETROS VOY A PASAR A CADA MÉTODO ESTÁTICO EL Escuela_ID ()
ayuda.Helper(
        listDictFinal,
        dfnom,
        df_FluidezLectora_1,
        mat_Escuela_ID_Curso,
        mat_Escuela_ID_Curso_División,
        FL_1_mat_Escuela_ID_Curso,
        FL_1_mat_Escuela_ID_Curso_División,
        df_Desempeño_por_Escuela,
        df_Desempeño_por_Escuela_CURSO_NORMALIZADO,
        df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,
        df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,
        df_Desempeño_por_Nivel_CURSO_NORMALIZADO)

for Escuela_ID in Escuelas_IDs:
    ayuda.Helper.lista_de_cursos_escuela(Escuela_ID)
    ayuda.Helper.matricula_por_escuela(Escuela_ID)
    ayuda.Helper.matricula_por_curso(Escuela_ID)
    ayuda.Helper.matricula_por_curso_división(Escuela_ID)    
    ayuda.Helper.matricula_por_escuela_fluidez_lectora_1(Escuela_ID)

    if ayuda.Helper.matriculaPorEscuela_FluidezLectora_1 != 0 :
        ayuda.Helper.listado_de_cursos_fluidez_lectora_1(Escuela_ID)
        ayuda.Helper.matricula_por_curso_fluidez_lectora_1(Escuela_ID)
        ayuda.Helper.matricula_por_curso_y_división_fluidez_lectora_1(Escuela_ID)

        ayuda.Helper.desempeño_por_escuela(Escuela_ID)
        ayuda.Helper.desempeño_por_escuela_y_curso(Escuela_ID)
        ayuda.Helper.desempeño_por_escuela_curso_y_division(Escuela_ID)
        ayuda.Helper.desempeño_por_curso_supervisión_y_nivel(Escuela_ID)
        
        ayuda.Helper.listado_de_alumnos_fluidez_lectora(Escuela_ID)


print('----------------------------------------------------------------')
dataDict = lib.UTILS.utils.obtener_data_de_la_lista(
    listDictFinal, 
    'Escuela_ID',
    9, 
    [
        'props' 
    ]
)
#lib.utils.imprimirDiccionario(dataDict)
print('----------------------------------------------------------------')
lib.UTILS.utils.grabar_diccionario_en_json(dataDict, carpeta + r'/BasesDeSalida/9_json.json')


print('..................FIN DEMO 0.........................!!!')