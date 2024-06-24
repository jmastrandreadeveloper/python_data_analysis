
import sys
import os
import pandas as pd
import random
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

import Módulos.GruposYFiltros.ObjetosFiltros.filtros

class Helper:


    def __init__(
            self,
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
            df_filtro_por_escuela_curso_division):
        
        Helper.listDictFinal = listDictFinal
        Helper.dfnom = dfnom
        Helper.df_FluidezLectora_1 = df_FluidezLectora_1
        Helper.mat_Escuela_ID_Curso = mat_Escuela_ID_Curso
        Helper.mat_Escuela_ID_Curso_División = mat_Escuela_ID_Curso_División
        Helper.FL_1_mat_Escuela_ID_Curso = FL_1_mat_Escuela_ID_Curso
        Helper.FL_1_mat_Escuela_ID_Curso_División = FL_1_mat_Escuela_ID_Curso_División
        Helper.df_Desempeño_por_Escuela = df_Desempeño_por_Escuela
        Helper.df_Desempeño_por_Escuela_CURSO_NORMALIZADO = df_Desempeño_por_Escuela_CURSO_NORMALIZADO
        Helper.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division
        Helper.df_Desempeño_por_Supervisión_CURSO_NORMALIZADO = df_Desempeño_por_Supervisión_CURSO_NORMALIZADO
        Helper.df_Desempeño_por_Nivel_CURSO_NORMALIZADO = df_Desempeño_por_Nivel_CURSO_NORMALIZADO
        Helper.df_filtro_por_escuela_curso_division = df_filtro_por_escuela_curso_division
        return
    
   
    @staticmethod
    def datos_institucionales(Escuela_ID):
        Helper.datosInstitucionales_dict = Módulos.GruposYFiltros.PorEscuela.por_escuela.filtrar_datos_institucionales_por_escuela(
            Escuela_ID,
            Helper.dfnom            
        )

        return Helper.datosInstitucionales_dict
    
    @staticmethod
    def lista_de_cursos_escuela(Escuela_ID):
        Helper.lista_de_cursos = Módulos.GruposYFiltros.PorEscuela.por_escuela.lista_de_cursos_escuela(
            Helper.dfnom,
            Escuela_ID
        )
        
        return Helper.lista_de_cursos


    @staticmethod
    def matricula_por_escuela(Escuela_ID):        
        return Módulos.GruposYFiltros.PorEscuela.por_escuela.filtrar_matricula_por_escuela(
            Helper.dfnom,
            Escuela_ID
        )
    
    @staticmethod
    def matricula_por_curso(Escuela_ID):
        Helper.matricula_por_curso_df = Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso.filtrar_matricula_por_escuela_y_curso(
            Helper.mat_Escuela_ID_Curso,
            Escuela_ID
        )

        return lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            Helper.matricula_por_curso_df
        )
    
    @staticmethod
    def matricula_por_curso_división(Escuela_ID):
        Helper.matricula_por_curso_división_tabla = {}
        Helper.dict_matricula_por_curso_division = Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división.filtrar_matricula_por_escuela_curso_y_division(
            Helper.mat_Escuela_ID_Curso_División,
            Escuela_ID,
            Helper.lista_de_cursos
        )
        for Curso in Helper.lista_de_cursos:
            # saco el dataframe qu está dentro del diccionario
            Helper.matricula_por_curso_división_tabla[Curso] = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                Helper.dict_matricula_por_curso_division.get(Curso))
            
        return Helper.matricula_por_curso_división_tabla
    
    @staticmethod
    def matricula_por_escuela_fluidez_lectora_1(Escuela_ID):
        Helper.matriculaPorEscuela_FluidezLectora_1 = Módulos.GruposYFiltros.PorEscuela.por_escuela.filtrar_matricula_por_escuela(
            Helper.df_FluidezLectora_1 ,
            Escuela_ID
        )

        return Helper.matriculaPorEscuela_FluidezLectora_1
    
    @staticmethod
    def listado_de_cursos_fluidez_lectora_1(Escuela_ID):
        Helper.lista_de_cursos_fluidez_lectora_1 = Módulos.GruposYFiltros.PorEscuela.por_escuela.lista_de_cursos_escuela(
            Helper.df_FluidezLectora_1,
            Escuela_ID
        )

        return Helper.lista_de_cursos_fluidez_lectora_1

    @staticmethod
    def matricula_por_curso_fluidez_lectora_1(Escuela_ID):
        Helper.matriculaPorCurso_FluidezLectora_1_df = Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso.filtrar_matricula_por_escuela_y_curso(
            Helper.FL_1_mat_Escuela_ID_Curso,
            Escuela_ID
        )

        return lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            Helper.matriculaPorCurso_FluidezLectora_1_df
        )
    
    @staticmethod
    def matricula_por_curso_y_división_fluidez_lectora_1(Escuela_ID):
        dict_matriculaPorCursoYDivision_FluidezLectora_1 = Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división.filtrar_matricula_por_escuela_curso_y_division(
            Helper.FL_1_mat_Escuela_ID_Curso_División,
            Escuela_ID,
            Helper.lista_de_cursos_fluidez_lectora_1
        )
        Helper.matricula_por_curso_división_fluidez_lectora_1_tabla = {}
        for Curso in Helper.lista_de_cursos_fluidez_lectora_1:
            Helper.matricula_por_curso_división_fluidez_lectora_1_tabla[Curso] = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                dict_matriculaPorCursoYDivision_FluidezLectora_1.get(Curso)
            )
            
        return Helper.matricula_por_curso_división_fluidez_lectora_1_tabla
    
    @staticmethod
    def desempeño_por_escuela(Escuela_ID):
        [Helper.desempeño_por_escuela_df,
        Helper.total_alumnos_por_escuela_df] = Módulos.GruposYFiltros.PorEscuela.por_escuela.filtrar_por_escuela(
            Escuela_ID,
            Helper.df_Desempeño_por_Escuela
        )

        Helper.dict_desempeño_por_escuela_df = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Pie_ChartJS(
            Helper.desempeño_por_escuela_df,
            'Desempeño_por_Escuela',
            'Desempeño de la Escuela en porcentaje'
        )
        Helper.total_alumnos_por_escuela_fluidez_lectora_1_tabla = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            Helper.total_alumnos_por_escuela_df             
        )

        return Helper.dict_desempeño_por_escuela_df
    
    @staticmethod
    def desempeño_por_escuela_y_curso(Escuela_ID):
        [Helper.desempeño_por_curso_df ,
        Helper.total_alumnos_por_tipo_de_desempeño_por_curso_df] = Módulos.GruposYFiltros.PorEscuela.por_escuela_y_curso.filtrar_por_escuela_y_curso(
            Escuela_ID,
            Helper.df_Desempeño_por_Escuela_CURSO_NORMALIZADO,
            Helper.lista_de_cursos_fluidez_lectora_1
        )

        Helper.dict_desempeño_por_curso_Bar_ChartJS = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
            Helper.desempeño_por_curso_df
        )

        Helper.total_alumnos_por_tipo_de_desempeño_por_curso = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            Helper.total_alumnos_por_tipo_de_desempeño_por_curso_df             
        )

        return Helper.dict_desempeño_por_curso_Bar_ChartJS       
    
    @staticmethod
    def desempeño_por_escuela_curso_y_division(Escuela_ID):
        Helper.dict_desempeño_por_curso_y_division_Bar_ChartJS = {}
        Helper.dict_total_alumnos_por_tipo_de_desempeño_por_curso_división1_tabla = {}
        [Helper.dict_desempeño_por_curso_division,
         Helper.dict_total_alumnos_por_tipo_de_desempeño_por_curso_división] = Módulos.GruposYFiltros.PorEscuela.por_escuela_curso_y_división.filtrar_por_escuela_curso_y_division(
            Escuela_ID,
            Helper.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,
            Helper.lista_de_cursos_fluidez_lectora_1
        )
        for Curso in Helper.lista_de_cursos_fluidez_lectora_1:
            Helper.desempeño_por_curso_division_df = Helper.dict_desempeño_por_curso_division.get(Curso)
            Helper.dict_desempeño_por_curso_y_division_Bar_ChartJS[Curso] = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
                Helper.desempeño_por_curso_division_df
            )
            Helper.total_alumnos_por_tipo_de_desempeño_por_curso_división_df = Helper.dict_total_alumnos_por_tipo_de_desempeño_por_curso_división.get(Curso)
            Helper.dict_total_alumnos_por_tipo_de_desempeño_por_curso_división1_tabla[Curso] = lib.UTILS.DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                Helper.total_alumnos_por_tipo_de_desempeño_por_curso_división_df             
            )

        return Helper.dict_desempeño_por_curso_y_division_Bar_ChartJS
    
    @staticmethod
    def desempeño_por_curso_supervisión_y_nivel(Escuela_ID):
        Helper.dict_desempeño_por_curso_supervisión_y_nivel_Bar_ChartJS = {}

        gradoAño = 'Grado' if Helper.datosInstitucionales_dict.get('Nivel') == 'Primario' else 'Año'
        Supervisión = Helper.datosInstitucionales_dict.get('Supervisión')
        Nivel = Helper.datosInstitucionales_dict.get('Nivel_Unificado')

        #filtro por supervision...
        Helper.desempeño_por_supervision_curso_df = Módulos.GruposYFiltros.PorSupervisión.por_supervisión_y_curso.filtrar_por_supervisión_y_curso(   
            Supervisión,
            Helper.df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,
            Helper.lista_de_cursos_fluidez_lectora_1
        )        
        # filtro por nivel al que pertenece la escuela...
        Helper.desempeño_por_nivel_curso_df = Módulos.GruposYFiltros.PorNivel.por_nivel_y_curso.filtrar_por_nivel_y_curso(
            Nivel,
            Helper.df_Desempeño_por_Nivel_CURSO_NORMALIZADO,
            Helper.lista_de_cursos_fluidez_lectora_1
        )
        # por cada curso que ha participado en el operativo, debo sacar obtener la columna correspondiente a 
        # a ese curso de cada uno de los tres dataframes, fusionarlos y convertirlos al formato de ChartJS
        for Curso in Helper.lista_de_cursos_fluidez_lectora_1:
            desempeño_por_curso_df = lib.UTILS.utils.copiar_columna_dataframe_a_otro_dataframe(Helper.desempeño_por_curso_df , Curso , Curso + ' ' + gradoAño)
            desempeño_por_supervision_curso_df = lib.UTILS.utils.copiar_columna_dataframe_a_otro_dataframe(Helper.desempeño_por_supervision_curso_df , Curso , Curso + ' ' + gradoAño + ' Sup. ' + Supervisión)
            desempeño_por_nivel_curso_df = lib.UTILS.utils.copiar_columna_dataframe_a_otro_dataframe(Helper.desempeño_por_nivel_curso_df , Curso , Curso + ' ' + gradoAño + ' Niv. ' + Nivel)
            # ahora lo que debo hacer es unir los dos dataframes
            # Unir los DataFrames
            Helper.desempeño_por_curso_supervisión_y_nivel_df = lib.UTILS.utils.join_dfs_on_index(
                [
                    desempeño_por_curso_df,
                    desempeño_por_supervision_curso_df,
                    desempeño_por_nivel_curso_df
                ],
                how='outer'
            )
            # traducir el dataframe al formato de barras de ChartJS
            Helper.dict_desempeño_por_curso_supervisión_y_nivel_Bar_ChartJS[Curso] = lib.UTILS.DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
                Helper.desempeño_por_curso_supervisión_y_nivel_df
            ) 

        return Helper.dict_desempeño_por_curso_supervisión_y_nivel_Bar_ChartJS
    
    # @staticmethod
    # def dispersión_por_escuela_curso_división(Escuela_ID):
    #     Helper.dict_dispersión_por_curso_division = lib.DATA.desempeñoEscolar2.FL_ESCUELA_003_desempeño_por_curso_division(
    #         Escuela_ID,
    #         Helper.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,
    #         Helper.lista_de_cursos_fluidez_lectora_1
    #     )
    #     return
    
    
    @staticmethod
    def listado_de_alumnos_fluidez_lectora(Escuela_ID):
        # SACAMOS EL LISTADO DE ALUMNOS DE TODA LA ESCUELA
        Helper.dict_listado_de_alumnos = Módulos.GruposYFiltros.PorEscuela.por_escuela.listado_de_alumnos(
            Escuela_ID,
            Helper.df_FluidezLectora_1,
            configDemo.listado_de_alumnos
        )

        return Helper.dict_listado_de_alumnos
    
    @staticmethod
    def obtener_filtro_por_escuela_curso_y_division(Escuela_ID):
        Helper.filtro_escuela_curso_division = Módulos.GruposYFiltros.ObjetosFiltros.filtros.obtener_filtro_por_escuela_curso_y_division(
            Escuela_ID,
            Helper.df_filtro_por_escuela_curso_division,
            Helper.lista_de_cursos_fluidez_lectora_1
        )
        
        return Helper.filtro_escuela_curso_division