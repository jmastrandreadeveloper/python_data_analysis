#from src.my_models_._abstract_model_.AbstractReport import AbstractReport
import src.tools.utils as u
import src.tools.DataFrameToCharJS as DataFrameToCharJS
import src.tools.DataFrameToDict as DataFrameToDict
import src.tools.DataFrameToDict as DataFrameToDict
import src.tools.DataFrameToTabla as DataFrameToTabla
import src.tools.DictToDataFrame as DictToDataFrame
from src.my_models_.__Nominal_para_fluidez_Lectora_1_.Main import Main as mainNominal
from src.my_models_.__Análisis_Fluidez_Lectora_1_.Main import Main as mainFluidezLectora
from src.my_models_.____Filtros.Filtro import Filtro
# from src.my_models_.__Nominal_para_fluidez_Lectora_1_.Report import Report as rNom
# from src.my_models_.__Análisis_Fluidez_Lectora_1_.Report import Report as rAFL
import pandas as pd

from src.my_models_.____Filtros.funciones.datos_institucionales import datos_institucionales
from src.my_models_.____Filtros.funciones.matricula_por_escuela import matricula_por_escuela
from src.my_models_.____Filtros.funciones.desempeño_por_escuela import desempeño_por_escuela
from src.my_models_.____Filtros.funciones.lista_de_cursos_escuela import lista_de_cursos_escuela
from src.my_models_.____Filtros.funciones.listado_de_alumnos import listado_de_alumnos
from src.my_models_.____Filtros.funciones.matricula_por_escuela_y_curso import matricula_por_escuela_y_curso
from src.my_models_.____Filtros.funciones.matricula_por_escuela_curso_y_division import matricula_por_escuela_curso_y_division

class ReporteEscuela : #(AbstractReport):
    def __init__(self, nominal : mainNominal , fluidez : mainFluidezLectora):
        self.nominal = nominal
        self.Fl = fluidez
        self.filtro = Filtro(nominal,fluidez)

    def do_report(self):
        self.do_report_escuela()
    
    def do_report_escuela(self, *args, **kwargs): 
        print('reporte por escuela de fluidez lectora')

        # listDictFinal será una lista de diccionarios, 
        # cada diccionario en la lista listDictFinal tendrá los datos de la escuela y 
        # todos los datos filtrados de fluidez lectora
        # esa lista se podrá recorrer para poder sacar luego los datos de la escuela 
        # que nosostros queramos...
        # cada uno de los diccionarios que va a mantener dentro va a tener como clave 
        # el id de la escuela..
        self.listDictFinal = []
        self.dictDatos = {
            'Escuela_ID' : None,
            'datos institucionales' : None
        }
        for Escuela_ID in self.nominal.listaEscuelas_IDs:
            dictDatos = {
                'Escuela_ID' : Escuela_ID,
                'data' : {
                    'datos_institucionales' : self.filtro._nominal_df_nominal_datos_institucionales(Escuela_ID),                    
                    'lista_de_cursos_escuela' : self.filtro._nominal_lista_de_cursos_escuela(Escuela_ID),
                    'matricula_por_escuela' : self.filtro._nominal_df_Escuela_ID_Alumno_ID_count(Escuela_ID),
                    'matricula_por_escuela_curso' : self.filtro._nominal_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count(Escuela_ID),
                    'matricula_por_escuela_curso_división' : self.filtro._nominal_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count(Escuela_ID),
                    'fluidez lectora 1' : {
                       'matricula_por_escuela_fluidez_lectora_1' : self.filtro._fluidez_df_Escuela_ID_Alumno_ID_count(Escuela_ID),
                    }
                }
            }
            # cuando tengo datos procesados de fluidez 1
            if dictDatos['data']['fluidez lectora 1']['matricula_por_escuela_fluidez_lectora_1'] != 0 :                
                dictDatosFluidez_Lectora = {                    
                    'matricula_por_escuela_fluidez_lectora_1' : self.filtro._fluidez_df_Escuela_ID_Alumno_ID_count(Escuela_ID),
                    'listado_de_cursos_fluidez_lectora_1' : self.filtro._fluidez_lista_de_cursos_escuela(Escuela_ID),
                    'matricula_por_curso_fluidez_lectora_1' : self.filtro._fluidez_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count(Escuela_ID),
                    'matricula_por_curso_y_división_fluidez_lectora_1' : self.filtro._fluidez_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count(Escuela_ID),
                    'desempeño_por_escuela' : self.filtro._fluidez_df_Desempeño_por_Escuela(Escuela_ID),
                    'desempeño_por_escuela_y_curso' : self.filtro._fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO(Escuela_ID),
                    'total_alumnos_por_tipo_de_desempeño_por_curso' : self.filtro._fluidez_total_alumnos_por_desempeño_por_escuela_y_curso(Escuela_ID),
                    'desempeño_por_escuela_curso_y_division' : self.filtro._fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division(Escuela_ID),
                }

                # reemplazdo la clave de fl anterior con la nueva generada
                dictDatos['data']['fluidez lectora 1'] = dictDatosFluidez_Lectora

            self.listDictFinal.append(dictDatos)
        print(dictDatos)
        dataDict = u.obtener_data_de_la_lista(
            self.listDictFinal,
            'Escuela_ID',
            9,
            [
                'data'
            ]
        )
        print(dataDict)
        u.imprimirDiccionario(dataDict)
        pass
    
    def datos_institucionales(self,Escuela_ID , dfnom ):
        datosInstitucionales_dict = datos_institucionales(
            Escuela_ID,
            dfnom            
        )
        return datosInstitucionales_dict
    
    def lista_de_cursos_escuela(self,Escuela_ID , dfnom):
        lista_de_cursos = lista_de_cursos_escuela(
            Escuela_ID,
            dfnom            
        )        
        return lista_de_cursos
        
    def matricula_por_escuela(self,Escuela_ID,dfnom):        
        return matricula_por_escuela(
            Escuela_ID,
            dfnom,            
        )    
    
    def matricula_por_escuela_y_curso(self,Escuela_ID,_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count):
        matricula_por_curso_df = matricula_por_escuela_y_curso(            
            Escuela_ID,
            _df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count
        )
        return DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            matricula_por_curso_df
        )
    
    
    def matricula_por_escuela_curso_división(self,Escuela_ID , _df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count , lista_de_cursos) :
        matricula_por_curso_división_tabla = {}
        dict_matricula_por_curso_division = matricula_por_escuela_curso_y_division(
            Escuela_ID,
            _df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,
            lista_de_cursos
        )
        for Curso in lista_de_cursos:
            # saco el dataframe qu está dentro del diccionario
            matricula_por_curso_división_tabla[Curso] = DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                dict_matricula_por_curso_division.get(Curso))
            
        return matricula_por_curso_división_tabla
    
    """
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
    """