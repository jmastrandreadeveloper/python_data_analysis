# esta clase estática servirá para poder iterar sobre los métodos de ella
# además va a permitir que se pueda configurar para que exporte en diferentes
# formatos gráficos o que queden como diccionarios

import sys
import os
import pandas as pd
# la clave está en pasar los paths en done está la libreria y en donde está la demo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería
import DemoPathConfigs as dPC
import ConfigDemoDataAnalisis_v2 as configDemo

import Módulos.GruposYFiltros.PorEscuela.por_escuela
import Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso
import Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división

import Módulos.GruposYFiltros.PorSupervisión.por_supervisión_y_curso

import Módulos.GruposYFiltros.PorNivel.por_nivel_y_curso


class Helper2:
    def __init__(
            self,
            _config,
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
            df_Desempeño_por_Nivel_CURSO_NORMALIZADO):
        
        Helper2._config = _config
        Helper2.listDictFinal = listDictFinal
        Helper2.dfnom = dfnom
        Helper2.df_FluidezLectora_1 = df_FluidezLectora_1
        Helper2.mat_Escuela_ID_Curso = mat_Escuela_ID_Curso
        Helper2.mat_Escuela_ID_Curso_División = mat_Escuela_ID_Curso_División
        Helper2.FL_1_mat_Escuela_ID_Curso = FL_1_mat_Escuela_ID_Curso
        Helper2.FL_1_mat_Escuela_ID_Curso_División = FL_1_mat_Escuela_ID_Curso_División
        Helper2.df_Desempeño_por_Escuela = df_Desempeño_por_Escuela
        Helper2.df_Desempeño_por_Escuela_CURSO_NORMALIZADO = df_Desempeño_por_Escuela_CURSO_NORMALIZADO
        Helper2.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division
        Helper2.df_Desempeño_por_Supervisión_CURSO_NORMALIZADO = df_Desempeño_por_Supervisión_CURSO_NORMALIZADO
        Helper2.df_Desempeño_por_Nivel_CURSO_NORMALIZADO = df_Desempeño_por_Nivel_CURSO_NORMALIZADO

        print(_config)
        return
    
    @staticmethod
    def lista_de_cursos_escuela(Escuela_ID):
        ##################################################################################################################################
        # OBTENEMOS LA LISTA DE CURSOS
        ##################################################################################################################################
        Helper2.lista_de_cursos = Módulos.GruposYFiltros.PorEscuela.por_escuela.lista_de_cursos_escuela(
            Helper2.dfnom,
            Escuela_ID
        )
        @staticmethod
        def insertar_lista_de_cursos_escuela():
            ##################################################################################################################################
            # INSERTAMOS TAMBIÉN LA LISTA DE CURSOS QUE TIENE LA ESCUELA
            ##################################################################################################################################
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal, 
                'Escuela_ID', 
                [
                    'props' 
                ], 
                Escuela_ID, 
                'lista_de_cursos', 
                Helper2.lista_de_cursos
            )
            return
        insertar_lista_de_cursos_escuela()        
        return    
    
    


    @staticmethod
    def matricula_por_escuela(Escuela_ID):
        ##################################################################################################################################
        # CALCULAMOS LA MATRÍCULA POR ESCUELA
        ##################################################################################################################################
        Helper2.matriculaPorEscuela = Módulos.GruposYFiltros.PorEscuela.por_escuela.filtrar_matricula_por_escuela(
            Helper2.dfnom,
            Escuela_ID
        )
        def insertar_matricula_por_escuela():
            ##################################################################################################################################
            # INSERTAMOS EL DATO DE LA MATRÍCULA POR ESCUELA
            ##################################################################################################################################
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal,
                'Escuela_ID' , 
                [
                    'props' , 
                    'matrícula institucional'
                ],
                Escuela_ID, 
                'matricula_por_escuela' , 
                Helper2.matriculaPorEscuela
            )
            return
        insertar_matricula_por_escuela()
        return    
    
    
    
    @staticmethod
    def matricula_por_curso(Escuela_ID):
        ##################################################################################################################################
        # MATRÍCULA POR CURSO
        ##################################################################################################################################
        Helper2.matricula_por_curso_df = Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso.filtrar_matricula_por_escuela_y_curso(
            Helper2.mat_Escuela_ID_Curso,
            Escuela_ID
        )
        def convertir_matricula_por_curso():
            ##################################################################################################################################
            # CONVIERTO LA MATRÍCULA POR CURSO EN UNA TABLA
            ##################################################################################################################################
            Helper2.matricula_por_curso_tabla = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                Helper2.matricula_por_curso_df
            )        
            return
    
        def insertar_matricula_por_curso():    
            # ##################################################################################################################################
            # # INSERTAMOS LA TABLA MATRÍCULA POR CURSO
            # ##################################################################################################################################
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal , 
                'Escuela_ID' , 
                [
                    'props' , 
                    'matrícula institucional'
                ]  , 
                Escuela_ID, 
                'matricula_por_curso' , 
                Helper2.matricula_por_curso_tabla
            )
            return
        return    
    
    
    
    @staticmethod
    def matricula_por_curso_división(Escuela_ID):
        ##################################################################################################################################
        # MATRÍCULA POR CURSO Y DIVISIÓN LE PASAMOS LA LISTA DE CURSOS DE LA ESCUELA
        ##################################################################################################################################
        Helper2.dict_matricula_por_curso_division = Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división.filtrar_matricula_por_escuela_curso_y_division(
            Helper2.mat_Escuela_ID_Curso_División,
            Escuela_ID,
            Helper2.lista_de_cursos
        )
        ##################################################################################################################################
        # INSERTAMOS LA MATRÍCULA POR CURSO Y DIVISIÓN
        # PERO PARA HACER ESTA OPERACIÓN, NECESITO ITERAR SOBRE EL LISTADO DE CURSOS
        # PORQUE LA FUNCIÓN ANTERIOR ME DEVOLVIÓ UN DICCIONARIO Y AHORA DEBO INSERTARLO
        # SIGUIENDO LA IDEA DE QUE ES UNA TABLA DE DATOS
        ##################################################################################################################################
        for Curso in Helper2.lista_de_cursos:
            # saco el dataframe qu está dentro del diccionario
            Helper2.matricula_por_curso_división_tabla = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                Helper2.dict_matricula_por_curso_division.get(Curso))
            # luego lo inserto, dentro de la clave 'matricula_por_curso_division' y 
            # a su vez dentro de la clave que sale de 'Curso'
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal , 
                'Escuela_ID' , 
                [
                    'props' , 
                    'matrícula institucional',
                    'matricula_por_curso_division'
                ]  , 
                Escuela_ID, 
                Curso, 
                Helper2.matricula_por_curso_división_tabla
            )
        return
    
    @staticmethod
    def matricula_por_escuela_fluidez_lectora_1(Escuela_ID):
        # MATRÍCULA DE FLUIDEZ LECTORA 1 POR ESCUELA
        # ES LA MATRÍCULA TOTAL CENSADA EN EL OPERATIVO
        ##################################################################################################################################
        Helper2.matriculaPorEscuela_FluidezLectora_1 = Módulos.GruposYFiltros.PorEscuela.por_escuela.filtrar_matricula_por_escuela(
            Helper2.df_FluidezLectora_1 ,
            Escuela_ID
        )
        ##################################################################################################################################
        # INSERTAMOS LA MATRÍCULA QUE PARTICIPÓ EN FLUIDEZ LECTORA 1
        ##################################################################################################################################
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props' , 
                'Fluidez Lectora 1',
                'matrícula fluidez lectora 1'
            ]  ,
            Escuela_ID , 
            'matricula_por_escuela' , 
            Helper2.matriculaPorEscuela_FluidezLectora_1
        )
        return
    
    @staticmethod
    def listado_de_cursos_fluidez_lectora_1(Escuela_ID):
        Helper2.lista_de_cursos_fluidez_lectora_1 = Módulos.GruposYFiltros.PorEscuela.por_escuela.lista_de_cursos_escuela(
            Helper2.df_FluidezLectora_1,
            Escuela_ID
        ) 
        ##################################################################################################################################
        # INSERTAMOS LA LISTA DE CURSOS QUE PARTICIPARON EN FLUIDEZ LECTORA
        ##################################################################################################################################
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal, 
            'Escuela_ID', 
            [
                'props',
                'Fluidez Lectora 1',
            ], 
            Escuela_ID, 
            'lista_de_cursos_fluidez_lectora_1', 
            Helper2.lista_de_cursos_fluidez_lectora_1
        )
        return

    @staticmethod
    def matricula_por_curso_fluidez_lectora_1(Escuela_ID):
        ##################################################################################################################################
        # MATRÍCULA DE FLUIDEZ LECTORA 1 POR ESCUELA Y CURSO
        # ES LA MATRÍCULA POR CADA UNO DE LOS CURSOS QUE PARTICIPARON EN EL  OPERATIVO
        ##################################################################################################################################
        Helper2.matriculaPorCurso_FluidezLectora_1_df = Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso.filtrar_matricula_por_escuela_y_curso(
            Helper2.FL_1_mat_Escuela_ID_Curso,
            Escuela_ID
        )
        ##################################################################################################################################
        # CONVIERTO LA MATRÍCULA POR CURSO DE FLUIDEZ LECTORA EN UNA TABLA
        ##################################################################################################################################
        Helper2.matricula_por_curso_FluidezLectora_1_tabla = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            Helper2.matriculaPorCurso_FluidezLectora_1_df
        )
        ##################################################################################################################################
        # INSERTAMOS LA MATRÍCULA POR CURSO QUE PARTICIPÓ EN FLUIDEZ LECTORA 1
        ##################################################################################################################################
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props' ,
                'Fluidez Lectora 1',
                'matrícula fluidez lectora 1'
            ]  , 
            Escuela_ID , 
            'matricula_por_curso' , 
            Helper2.matricula_por_curso_FluidezLectora_1_tabla
        )
        return
    
    @staticmethod
    def filtrar_por_escuela_curso_y_division(Escuela_ID, CURSO_NORMALIZADO , División ):
        return f"(Escuela_ID == {Escuela_ID}) & (CURSO_NORMALIZADO == '{CURSO_NORMALIZADO}') & (División == '{División}')"
    
    @staticmethod
    def matricula_por_curso_y_división_fluidez_lectora_1(Escuela_ID):
        #################################################################################################################################
        # MATRÍCULA DE FLUIDEZ LECTORA 1 POR ESCUELA CURSO Y DIVISIÓN
        # ES LA MATRÍCULA POR CADA UNO DE LOS CURSOS Y DIVISIONES QUE PARTICIPARON EN EL  OPERATIVO
        ##################################################################################################################################        
        dict_matriculaPorCursoYDivision_FluidezLectora_1 = Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división.filtrar_matricula_por_escuela_curso_y_division(
            Helper2.FL_1_mat_Escuela_ID_Curso_División,
            Escuela_ID,
            Helper2.lista_de_cursos_fluidez_lectora_1
        )
        ##################################################################################################################################
        # INSERTAMOS LA MATRÍCULA POR ESCUELA CURSO Y DIVISIÓN QUE PARTICIPÓ EN FLUIDEZ LECTORA 1
        ##################################################################################################################################
        ##################################################################################################################################
        # INSERTAMOS LA MATRÍCULA POR CURSO Y DIVISIÓN
        # PERO PARA HACER ESTA OPERACIÓN, NECESITO ITERAR SOBRE EL LISTADO DE CURSOS
        # PORQUE LA FUNCIÓN ANTERIOR ME DEVOLVIÓ UN DICCIONARIO Y AHORA DEBO INSERTARLO
        # SIGUIENDO LA IDEA DE QUE ES UNA TABLA DE DATOS...DE LA MISMA MANERA QUE SE HIZO PARA EL NOMINAL
        ##################################################################################################################################
        for Curso in Helper2.lista_de_cursos_fluidez_lectora_1:
            # saco el dataframe qu está dentro del diccionario
            Helper2.matricula_por_curso_división_fluidez_lectora_1_tabla = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                dict_matriculaPorCursoYDivision_FluidezLectora_1.get(Curso))
            # luego lo inserto, dentro de la clave 'matricula_por_curso_division' y 
            # a su vez dentro de la clave que sale de 'Curso'
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal , 
                'Escuela_ID' , 
                [
                    'props' , 
                    'Fluidez Lectora 1',
                    'matrícula fluidez lectora 1',
                    'matricula_por_curso_division'
                ]  , 
                Escuela_ID, 
                Curso, 
                Helper2.matricula_por_curso_división_fluidez_lectora_1_tabla
            )
        return
    
    @staticmethod
    def desempeño_por_escuela(Escuela_ID):
        #################################################################################################################################
        # DESEMPEÑO POR ESCUELA
        ##################################################################################################################################
        [Helper2.desempeño_por_escuela_df,
        Helper2.total_alumnos_por_escuela_df] = Módulos.GruposYFiltros.PorEscuela.por_escuela.filtrar_por_escuela(
            Escuela_ID,
            Helper2.df_Desempeño_por_Escuela
        )
        
        ##################################################################################################################################
        # CONVIERTO EL DESEMPEÑO POR ESCUELA DE DATAFRAME A DICCIONARIO
        ##################################################################################################################################

        
        Helper2.dict_desempeño_por_escuela = lib.UTILS.DataFrameToDict.data_frame_to_diccionario(
            Helper2.desempeño_por_escuela_df
        )

        ##################################################################################################################################
        # INSERTAMOS DESEMPEÑO POR ESCUELA EN FORMATO DE DICCIONARIO
        ##################################################################################################################################
        
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props',
                'Fluidez Lectora 1',
                'desempeño_por_escuela_DICCIONARIO'
            ]  , 
            Escuela_ID ,
            'salida_dict_desempeño_por_escuela', 
            Helper2.dict_desempeño_por_escuela
        )


        ##################################################################################################################################
        # CONVERTIMOS EL DATAFRAME 'desempeño_por_escuela_df' PARA QUE SEA
        # INSERTADO CON EL FORMATO DE un Pie ChartJS
        ##################################################################################################################################
        Helper2.dict_desempeño_por_escuela_df = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Pie_ChartJS(
            Helper2.desempeño_por_escuela_df,
            'Desempeño_por_Escuela'
        )
        ##################################################################################################################################
        # INSERTAMOS DESEMPEÑO POR ESCUELA
        ##################################################################################################################################
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props',
                'Fluidez Lectora 1',
                'desempeño_por_escuela'
            ]  , 
            Escuela_ID ,
            'salida_ChartJS', 
            Helper2.dict_desempeño_por_escuela_df
        )
        ##################################################################################################################################
        # CONVERTIMOS EL DATAFRAME 'total_alumnos_por_escuela_df' PARA QUE SEA
        # INSERTADO COMO TABLA DE DATOS
        ##################################################################################################################################
        Helper2.total_alumnos_por_escuela_fluidez_lectora_1_tabla = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            Helper2.total_alumnos_por_escuela_df             
        )
        ##################################################################################################################################
        # INSERTAMOS LA TABLA total_alumnos_por_escuela_fluidez_lectora_1_tabla POR ESCUELA DE FL 1
        ##################################################################################################################################
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props',
                'Fluidez Lectora 1',
                'desempeño_por_escuela'
            ]  , 
            Escuela_ID ,
            'total_alumnos_por_escuela_fluidez_lectora_1_tabla',
            Helper2.total_alumnos_por_escuela_fluidez_lectora_1_tabla
        )
        return
    
    @staticmethod
    def desempeño_por_escuela_y_curso(Escuela_ID):
        ##################################################################################################################################
        # DESEMPEÑO POR ESCUELA Y CURSO
        ##################################################################################################################################
        [Helper2.desempeño_por_curso_df ,
        Helper2.total_alumnos_por_tipo_de_desempeño_por_curso_df] = Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso.filtrar_por_escuela_y_curso(
            Escuela_ID,
            Helper2.df_Desempeño_por_Escuela_CURSO_NORMALIZADO,
            Helper2.lista_de_cursos_fluidez_lectora_1
        )

        ##################################################################################################################################
        # CONVIERTO EL DESEMPEÑO POR ESCUELA Y CURSO DATAFRAME A DICCIONARIO
        ##################################################################################################################################

        
        Helper2.dict_desempeño_por_escuela_y_curso = lib.UTILS.DataFrameToDict.data_frame_to_diccionario(
            Helper2.desempeño_por_curso_df
        )

        ##################################################################################################################################
        # INSERTAMOS DESEMPEÑO POR ESCUELA Y CURSO EN FORMATO DE DICCIONARIO
        ##################################################################################################################################
        
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props',
                'Fluidez Lectora 1',
                'desempeño_por_escuela_y_curso_DICCIONARIO'
            ]  , 
            Escuela_ID ,
            'salida_dict_desempeño_por_escuela_y_curso', 
            Helper2.dict_desempeño_por_escuela_y_curso
        )





        ##################################################################################################################################
        # CONVERTIMOS EL DATAFRAME 'desempeño_por_curso_df' PARA QUE SEA
        # INSERTADO CON EL FORMATO DE un Pie ChartJS
        ##################################################################################################################################
        Helper2.dict_desempeño_por_curso_Bar_ChartJS = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
            Helper2.desempeño_por_curso_df
        )
        ##################################################################################################################################
        # INSERTAMOS DESEMPEÑO POR CURSO
        ##################################################################################################################################
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props',
                'Fluidez Lectora 1',
                'desempeño_por_escuela_y_curso'
            ]  , 
            Escuela_ID ,
            'salida_ChartJS', 
            Helper2.dict_desempeño_por_curso_Bar_ChartJS
        )        
        return
       
    
    @staticmethod
    def desempeño_por_escuela_curso_y_division(Escuela_ID):
        ##################################################################################################################################
        # DESEMPEÑO POR ESCUELA, CURSO Y DIVISIÓN
        ##################################################################################################################################
        [Helper2.dict_desempeño_por_curso_division,
         Helper2.dict_total_alumnos_por_tipo_de_desempeño_por_curso_división] = Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división.filtrar_por_escuela_curso_y_division(
            Escuela_ID,
            Helper2.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,
            Helper2.lista_de_cursos_fluidez_lectora_1
        )
        ##################################################################################################################################
        # INSERTAMOS EL DESEMPEÑO POR CURSO Y DIVISIÓN
        # PERO PARA HACER ESTA OPERACIÓN, NECESITO ITERAR SOBRE EL LISTADO DE CURSOS
        # PORQUE LA FUNCIÓN ANTERIOR ME DEVOLVIÓ UN DICCIONARIO Y AHORA DEBO INSERTARLO
        ##################################################################################################################################
        for Curso in Helper2.lista_de_cursos_fluidez_lectora_1:
            # saco el dataframe qu está dentro del diccionario
            Helper2.desempeño_por_curso_division_df = Helper2.dict_desempeño_por_curso_division.get(Curso)

            ##################################################################################################################################
            # CONVIERTO EL DESEMPEÑO POR ESCUELA Y CURSO DATAFRAME A DICCIONARIO
            ##################################################################################################################################

            
            Helper2.dict_desempeño_por_curso_division_ = lib.UTILS.DataFrameToDict.data_frame_to_diccionario(
                Helper2.desempeño_por_curso_division_df
            )

            ##################################################################################################################################
            # INSERTAMOS DESEMPEÑO POR ESCUELA Y CURSO EN FORMATO DE DICCIONARIO
            ##################################################################################################################################
            
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal , 
                'Escuela_ID' , 
                [
                    'props',
                    'Fluidez Lectora 1',
                    'desempeño_por_curso_division_DICCIONARIO'
                ]  , 
                Escuela_ID ,
                'salida_dict_desempeño_por_escuela_y_curso', 
                Helper2.dict_desempeño_por_curso_division_
            )




            # luego debo traducir el dataframe 'desempeño_por_curso_division_df' en el formato para ser
            # representado como un BarChartJS
            Helper2.dict_desempeño_por_curso_y_division_Bar_ChartJS = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
                Helper2.desempeño_por_curso_division_df
            )
            # y ahora lo inserto en la estructura..
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal , 
                'Escuela_ID' , 
                [
                    'props' , 
                    'Fluidez Lectora 1',                    
                    'desempeño_por_escuela_curso_y_división',
                    'salida_ChartJS'
                ]  , 
                Escuela_ID, 
                Curso,
                Helper2.dict_desempeño_por_curso_y_division_Bar_ChartJS
            )
            ##################################################################################################################################
            # INSERTAMOS EL EL TOTAL DE ALUMNOS POR CURSO Y DIVISIÓN CALCULADO ANTERIORMENTE Y LO
            # CONVERTIMOS A UNA TABLA DE DATOS
            ##################################################################################################################################
            Helper2.total_alumnos_por_tipo_de_desempeño_por_curso_división_df = Helper2.dict_total_alumnos_por_tipo_de_desempeño_por_curso_división.get(Curso)
            # lo convierto a tabla de datos
            Helper2.total_alumnos_por_tipo_de_desempeño_por_curso_división1_tabla = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                Helper2.total_alumnos_por_tipo_de_desempeño_por_curso_división_df             
            )
            ##################################################################################################################################
            # INSERTAMOS LA TABLA DE TOTAL DE ALUMNOS POR CURSO Y DIVISIÓN
            ##################################################################################################################################
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal , 
                'Escuela_ID' , 
                [
                    'props',
                    'Fluidez Lectora 1',
                    'desempeño_por_escuela_curso_y_división',                    
                ],
                Escuela_ID,
                'total_alumnos_por_tipo_de_desempeño_por_curso_división',
                Helper2.total_alumnos_por_tipo_de_desempeño_por_curso_división1_tabla
            )
        return
    
    @staticmethod
    def desempeño_por_curso_supervisión_y_nivel(Escuela_ID):
        # detectar si el nivel de la escuela es Primario o Secundario para poder determinar si usamos Año o Grado
        gradoAño = 'Grado' if lib.UTILS.utils.obtener_data_de_la_lista(
            Helper2.listDictFinal ,
            'Escuela_ID' ,
            Escuela_ID,
            [
                'props' ,
                'Nivel'
            ]
        ) == 'Primario' else 'Año'
        # nombre de la supervisión
        Supervisión = lib.UTILS.utils.obtener_data_de_la_lista(
            Helper2.listDictFinal ,
            'Escuela_ID' ,
            Escuela_ID,
            [
                'props' ,
                'Supervisión'
            ]
        )
        # nombre del Nivel
        # acá obtengo el nombre del nivel
        Nivel = lib.UTILS.utils.obtener_data_de_la_lista(
            Helper2.listDictFinal ,
            'Escuela_ID' ,
            Escuela_ID ,
            [
                'props' ,
                'Nivel_Unificado'
            ]
        )        
        # ya cuento con el dataframe 
        # del desempeño por curso 'Helper2.desempeño_por_curso_df',
        # no hay que volverlo a filtrarlo...!!!
        #filtro por supervision...
        Helper2.desempeño_por_supervision_curso_df = Módulos.GruposYFiltros.PorSupervisión.por_supervisión_y_curso.filtrar_por_supervisión_y_curso(   
            Supervisión,
            Helper2.df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,
            Helper2.lista_de_cursos_fluidez_lectora_1
        )        
        # filtro por nivel al que pertenece la escuela...
        Helper2.desempeño_por_nivel_curso_df = Módulos.GruposYFiltros.PorNivel.por_nivel_y_curso.filtrar_por_nivel_y_curso(
            Nivel,
            Helper2.df_Desempeño_por_Nivel_CURSO_NORMALIZADO,
            Helper2.lista_de_cursos_fluidez_lectora_1
        )
        # por cada curso que ha participado en el operativo, debo sacar obtener la columna correspondiente a 
        # a ese curso de cada uno de los tres dataframes, fusionarlos y convertirlos al formato de ChartJS
        for Curso in Helper2.lista_de_cursos_fluidez_lectora_1:
            desempeño_por_curso_df = lib.UTILS.utils.copiar_columna_dataframe_a_otro_dataframe(Helper2.desempeño_por_curso_df , Curso , Curso + ' ' + gradoAño)
            desempeño_por_supervision_curso_df = lib.UTILS.utils.copiar_columna_dataframe_a_otro_dataframe(Helper2.desempeño_por_supervision_curso_df , Curso , Curso + ' ' + gradoAño + ' Sup. ' + Supervisión)
            desempeño_por_nivel_curso_df = lib.UTILS.utils.copiar_columna_dataframe_a_otro_dataframe(Helper2.desempeño_por_nivel_curso_df , Curso , Curso + ' ' + gradoAño + ' Niv. ' + Nivel)
            # ahora lo que debo hacer es unir los dos dataframes
            # Unir los DataFrames
            Helper2.desempeño_por_curso_supervisión_y_nivel_df = lib.UTILS.utils.join_dfs_on_index(
                [
                    desempeño_por_curso_df,
                    desempeño_por_supervision_curso_df,
                    desempeño_por_nivel_curso_df
                ],
                how='outer'
            )
            # traducir el dataframe al formato de barras de ChartJS
            Helper2.dict_desempeño_por_curso_supervisión_y_nivel_Bar_ChartJS = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
                Helper2.desempeño_por_curso_supervisión_y_nivel_df
            )            
            # y ahora lo inserto en la estructura..
            Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
                Helper2.listDictFinal , 
                'Escuela_ID' , 
                [
                    'props' , 
                    'Fluidez Lectora 1',
                    'desempeño_por_escuela_curso_supervisión_y_nivel',
                    'salida_ChartJS'
                ]  , 
                Escuela_ID, 
                Curso,
                Helper2.dict_desempeño_por_curso_supervisión_y_nivel_Bar_ChartJS
            )

        return
    
    # @staticmethod
    # def dispersión_por_escuela_curso_división(Escuela_ID):
    #     Helper2.dict_dispersión_por_curso_division = lib.DATA.desempeñoEscolar2.FL_ESCUELA_003_desempeño_por_curso_division(
    #         Escuela_ID,
    #         Helper2.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,
    #         Helper2.lista_de_cursos_fluidez_lectora_1
    #     )
    #     return
    
    
    @staticmethod
    def listado_de_alumnos_fluidez_lectora(Escuela_ID):
        # SACAMOS EL LISTADO DE ALUMNOS DE TODA LA ESCUELA
        Helper2.dict_listado_de_alumnos = Módulos.GruposYFiltros.PorEscuela.por_escuela.listado_de_alumnos(
            Escuela_ID,
            Helper2.df_FluidezLectora_1,
            configDemo.listado_de_alumnos
        )
        # INSERTAMOS EL LISTADO DE ALUMNOS DE LA ESCUELA
        Helper2.listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            Helper2.listDictFinal , 
            'Escuela_ID' , 
            [
                'props',
                'Fluidez Lectora 1'
            ]  , 
            Escuela_ID , 
            'dict_listado_de_alumnos' , 
            Helper2.dict_listado_de_alumnos
        )
        return


    
    @staticmethod
    def actualizar_configuracion(nueva_config):
        """Actualiza la configuración de ejecución de los métodos."""
        for metodo, estado in nueva_config.items():
            if metodo in Helper2._config:
                Helper2._config[metodo] = estado

    
    @staticmethod
    def metodo1():
        """Ejemplo de método estático 1."""
        if not Helper2._config['metodo1']:
            print("metodo1 está deshabilitado.")
            return
        # Lógica del método 1
        print("Ejecutando metodo1")

    @staticmethod
    def metodo2():
        """Ejemplo de método estático 2."""
        if not Helper2._config['metodo2']:
            print("metodo2 está deshabilitado.")
            return
        # Lógica del método 2
        print("Ejecutando metodo2")

    @staticmethod
    def metodo3():
        """Ejemplo de método estático 3."""
        if not Helper2._config['metodo3']:
            print("metodo3 está deshabilitado.")
            return
        # Lógica del método 3
        print("Ejecutando metodo3")


    