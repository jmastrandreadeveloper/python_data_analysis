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

import Módulos.GruposYFiltros.ObjetosFiltros.filtros


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

# lista de todos los Escuelas_IDs (lista)
Escuelas_IDs = lib.UTILS.utils.obtener_datos_de_columna(
    dfnom, 
    'Escuela_ID',
    True
)

# genero la columna Nivel_Unificado
dfnom = Módulos.DataClean.clean_nominal.procesar_nominal_v2(dfnom)



# [listDictFinal , 
#  dictValues , 
#  Escuelas_IDs] = Módulos.DataClean.clean_nominal.procesar_nominal(dfnom)

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


df_filtro_por_escuela_curso_division = Módulos.GruposYFiltros.ObjetosFiltros.filtros.hacer_filtro_por_escuela_curso_y_division(
    df_FluidezLectora_1
)


# listDictFinal será una lista de diccionarios, 
# cada diccionario en la lista listDictFinal tendrá los datos de la escuela y 
# todos los datos filtrados de fluidez lectora
# esa lista se podrá recorrer para poder sacar luego los datos de la escuela 
# que nosostros queramos...
# cada uno de los diccionarios que va a mantener dentro va a tener como clave 
# el id de la escuela..
listDictFinal = []
dictDatos = {
    'Escuela_ID' : None,
    'datos institucionales' : None
}


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
        df_Desempeño_por_Nivel_CURSO_NORMALIZADO,
        df_filtro_por_escuela_curso_division)

for Escuela_ID in Escuelas_IDs:
    #ayuda.Helper.random_by_Escuela_ID(Escuela_ID) = 
    dictDatos = {
        'Escuela_ID' : Escuela_ID,
        'data' : {
            'datos_institucionales' : ayuda.Helper.datos_institucionales(Escuela_ID),
            'lista_de_cursos_escuela' : ayuda.Helper.lista_de_cursos_escuela(Escuela_ID),
            'matricula_por_escuela' : ayuda.Helper.matricula_por_escuela(Escuela_ID),
            'matricula_por_curso' : ayuda.Helper.matricula_por_curso(Escuela_ID),
            'matricula_por_curso_división' : ayuda.Helper.matricula_por_curso_división(Escuela_ID),
            'fluidez lectora 1' : {
                'matricula_por_escuela_fluidez_lectora_1' : ayuda.Helper.matricula_por_escuela_fluidez_lectora_1(Escuela_ID)
            }
        }
    }


    if ayuda.Helper.matriculaPorEscuela_FluidezLectora_1 != 0 :
        dictDatosFluidez_Lectora = {
            'matricula_por_escuela_fluidez_lectora_1' : ayuda.Helper.matricula_por_escuela_fluidez_lectora_1(Escuela_ID),
            'listado_de_cursos_fluidez_lectora_1' : ayuda.Helper.listado_de_cursos_fluidez_lectora_1(Escuela_ID),
            # acá va la generación de los filtros que se insertarán dentro de la estructura de diccionario que
            # henos creado, por lo tanto se deberàn construir acá los filtros.
            # los filtros trabajarán sobre fluidez lectora, es decir que se construiran a partir de esos datos, no 
            # NO debemos usar el nominal porque no sería correcto usar un filtro que puede no traernos nada...
            'filtro_escuela_curso_division' : ayuda.Helper.obtener_filtro_por_escuela_curso_y_division(Escuela_ID),
            'matricula_por_curso_fluidez_lectora_1' : ayuda.Helper.matricula_por_curso_fluidez_lectora_1(Escuela_ID),
            'matricula_por_curso_y_división_fluidez_lectora_1' : ayuda.Helper.matricula_por_curso_y_división_fluidez_lectora_1(Escuela_ID),
            'desempeño_por_escuela' : ayuda.Helper.desempeño_por_escuela(Escuela_ID),
            'total_alumnos_por_escuela_fluidez_lectora_1' : ayuda.Helper.total_alumnos_por_escuela_fluidez_lectora_1_tabla,
            'desempeño_por_escuela_y_curso' : ayuda.Helper.desempeño_por_escuela_y_curso(Escuela_ID),
            'total_alumnos_por_tipo_de_desempeño_por_curso' : ayuda.Helper.total_alumnos_por_tipo_de_desempeño_por_curso,
            'desempeño_por_escuela_curso_y_division' : ayuda.Helper.desempeño_por_escuela_curso_y_division(Escuela_ID),
            'total_alumnos_por_tipo_de_desempeño_por_curso_división' : ayuda.Helper.dict_total_alumnos_por_tipo_de_desempeño_por_curso_división1_tabla,
            'desempeño_por_curso_supervisión_y_nivel' : ayuda.Helper.desempeño_por_curso_supervisión_y_nivel(Escuela_ID),
            'listado_de_alumnos_fluidez_lectora' : ayuda.Helper.listado_de_alumnos_fluidez_lectora(Escuela_ID),            
        }
        # reemplazdo la clave de fl anterior con la nueva generada
        dictDatos['data']['fluidez lectora 1'] = dictDatosFluidez_Lectora
        
        ayuda.Helper.listado_de_alumnos_fluidez_lectora(Escuela_ID)
    listDictFinal.append(dictDatos)


# for el in ayuda.Helper.listDictFinal:
#     print(el)
print('----------------------------------------------------------------')
dataDict = lib.UTILS.utils.obtener_data_de_la_lista(
    listDictFinal, 
    'Escuela_ID',
    9, 
    [   
        'data'
    ]
)
#lib.UTILS.utils.imprimirDiccionario(dataDict)
print('----------------------------------------------------------------')
lib.UTILS.utils.grabar_diccionario_en_json(dataDict, carpeta + r'/BasesDeSalida/9_json.json')



print('..................FIN DEMO 2.........................!!!')