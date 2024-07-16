from src.my_models_.__Nominal_para_fluidez_Lectora_1_.Main import Main as mainNominal
from src.my_models_.__Análisis_Fluidez_Lectora_1_.Main import Main as mainFluidezLectora
import src.tools.utils as u
import src.tools.DataFrameToCharJS as DataFrameToCharJS
import src.tools.DataFrameToDict as DataFrameToDict
import src.tools.DataFrameToDict as DataFrameToDict
import src.tools.DataFrameToTabla as DataFrameToTabla
import src.tools.DictToDataFrame as DictToDataFrame
from src.my_models_.____Filtros.funciones.datos_institucionales import datos_institucionales
from src.my_models_.____Filtros.funciones.matricula_por_escuela import matricula_por_escuela
from src.my_models_.____Filtros.funciones.desempeño_por_escuela import desempeño_por_escuela
from src.my_models_.____Filtros.funciones.desempeño_por_escuela_y_curso import desempeño_por_escuela_y_curso
from src.my_models_.____Filtros.funciones.lista_de_cursos_escuela import lista_de_cursos_escuela
from src.my_models_.____Filtros.funciones.listado_de_alumnos import listado_de_alumnos
from src.my_models_.____Filtros.funciones.matricula_por_escuela_y_curso import matricula_por_escuela_y_curso
from src.my_models_.____Filtros.funciones.matricula_por_escuela_curso_y_division import matricula_por_escuela_curso_y_division
from src.my_models_.____Filtros.funciones.total_alumnos_por_desempeño_por_escuela_y_curso import total_alumnos_por_desempeño_por_escuela_y_curso
from src.my_models_.____Filtros.funciones.desempeño_por_escuela_curso_y_division import desempeño_por_escuela_curso_y_division

class Filtro : #(AbstractReport):
    
    def __init__(self, nominal : mainNominal , fluidez : mainFluidezLectora):        
        # extraigo todos los dataframes de ambos objetos
        # de la agrupación del nominal        
        self.nominal_df_nominal_datos_institucionales = nominal.df_nominal_datos_institucionales        
        self.nominal_df_Escuela_ID_CURSO_NORMALIZADO_list = nominal.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_list
        self.nominal_df_Escuela_ID_Alumno_ID_count = nominal.group_agg._df_Escuela_ID_Alumno_ID_count
        self.nominal_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = nominal.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count
        self.nominal_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count = nominal.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count
        self.nominal_df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count = nominal.group_agg._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count
        self.nominal_df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count = nominal.group_agg._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count
        # de la agrupación de fluidez
        self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_list = fluidez.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_list
        self.fluidez_df_Escuela_ID_Alumno_ID_count = fluidez.group_agg._df_Escuela_ID_Alumno_ID_count
        self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = fluidez.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count
        self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count = fluidez.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count
        self.fluidez_df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count = fluidez.group_agg._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count
        self.fluidez_df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count = fluidez.group_agg._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count
        # agrupamiento que son propios de este dataframe de fluidez lectora, estos agruipamientos están
        # en esta función., más abajo , son los que agrupan el desempeño y nos va a servir para poder
        # sacar los pocentajes de desempeño
        self.fluidez_df_Escuela_ID_DESEMPEÑO_Alumno_ID_count = fluidez.group_agg._df_Escuela_ID_DESEMPEÑO_Alumno_ID_count
        self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count = fluidez.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count
        self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count = fluidez.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count
        self.fluidez_df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count = fluidez.group_agg._df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count
        self.fluidez_df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count = fluidez.group_agg._df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count      
        # los desempeños calculados en el calculador de desempeños
        self.fluidez_df_Desempeño_por_Escuela = fluidez.calculador._df_Desempeño_por_Escuela
        self.fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO = fluidez.calculador._df_Desempeño_por_Escuela_CURSO_NORMALIZADO
        self.fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = fluidez.calculador._df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division
        self.fluidez_df_Desempeño_por_Supervisión_CURSO_NORMALIZADO = fluidez.calculador._df_Desempeño_por_Supervisión_CURSO_NORMALIZADO
        self.fluidez_df_Desempeño_por_Nivel_CURSO_NORMALIZADO = fluidez.calculador._df_Desempeño_por_Nivel_CURSO_NORMALIZADO
        pass

    
    def _nominal_df_nominal_datos_institucionales(self,Escuela_ID ):
        datosInstitucionales_dict = datos_institucionales(
            Escuela_ID,
            self.nominal_df_nominal_datos_institucionales            
        )
        return datosInstitucionales_dict
    
    
    def _nominal_lista_de_cursos_escuela(self,Escuela_ID):
        self.nominal_lista_de_cursos = lista_de_cursos_escuela(
            Escuela_ID,
            self.nominal_df_Escuela_ID_CURSO_NORMALIZADO_list
        )        
        return self.nominal_lista_de_cursos
        
    
    def _nominal_df_Escuela_ID_Alumno_ID_count(self,Escuela_ID):        
        return matricula_por_escuela(
            Escuela_ID,
            self.nominal_df_Escuela_ID_Alumno_ID_count,            
        )    
    
    def _nominal_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count(self,Escuela_ID):
        matricula_por_curso_df = matricula_por_escuela_y_curso(            
            Escuela_ID,
            self.nominal_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count
        )
        return DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            matricula_por_curso_df
        )
    
    def _nominal_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count(self,Escuela_ID) :
        matricula_por_curso_división_tabla = {}
        dict_matricula_por_curso_division = matricula_por_escuela_curso_y_division(
            Escuela_ID,
            self.nominal_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,
            self.nominal_lista_de_cursos
        )
        for Curso in self.nominal_lista_de_cursos:
            # saco el dataframe qu está dentro del diccionario
            matricula_por_curso_división_tabla[Curso] = DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                dict_matricula_por_curso_division.get(Curso))
            
        return matricula_por_curso_división_tabla
    
    def _fluidez_df_Escuela_ID_Alumno_ID_count(self,Escuela_ID):
        return matricula_por_escuela(
            Escuela_ID,
            self.fluidez_df_Escuela_ID_Alumno_ID_count,            
        )
    
    def _fluidez_lista_de_cursos_escuela(self,Escuela_ID):
        self.fluidez_1__lista_de_cursos = lista_de_cursos_escuela(
            Escuela_ID,
            self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_list
        )        
        return self.fluidez_1__lista_de_cursos
    
    def _fluidez_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count(self,Escuela_ID):
        matricula_por_curso_df = matricula_por_escuela_y_curso(            
            Escuela_ID,
            self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count
        )
        return DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            matricula_por_curso_df
        )
    

        
    def _fluidez_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count(self,Escuela_ID):
        matricula_por_curso_división_tabla = {}
        dict_matricula_por_curso_division = matricula_por_escuela_curso_y_division(
            Escuela_ID,
            self.fluidez_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,
            self.fluidez_1__lista_de_cursos
        )
        for Curso in self.fluidez_1__lista_de_cursos:
            # saco el dataframe qu está dentro del diccionario
            matricula_por_curso_división_tabla[Curso] = DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                dict_matricula_por_curso_division.get(Curso))
            
        return matricula_por_curso_división_tabla
    
    
    def _fluidez_df_Desempeño_por_Escuela(self,Escuela_ID):
        [desempeño_por_escuela_df,
        total_alumnos_por_escuela_df] = desempeño_por_escuela(
            Escuela_ID,
            self.fluidez_df_Desempeño_por_Escuela
        )

        dict_desempeño_por_escuela_df = DataFrameToCharJS.convertir_dataFrame_a_Pie_ChartJS(
            desempeño_por_escuela_df,
            'Desempeño_por_Escuela',
            'Desempeño de la Escuela en porcentaje'
        )
        total_alumnos_por_escuela_fluidez_lectora_1_tabla = DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            total_alumnos_por_escuela_df
        )

        return dict_desempeño_por_escuela_df    
    
    def _fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO(self,Escuela_ID):
        desempeño_por_curso_df = desempeño_por_escuela_y_curso(
            Escuela_ID,
            self.fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO,
            self.fluidez_1__lista_de_cursos
        )

        dict_desempeño_por_curso_Bar_ChartJS = DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
            desempeño_por_curso_df
        )

        return dict_desempeño_por_curso_Bar_ChartJS
    

    def _fluidez_total_alumnos_por_desempeño_por_escuela_y_curso(self,Escuela_ID):
        total_alumnos_por_tipo_de_desempeño_por_curso_df = total_alumnos_por_desempeño_por_escuela_y_curso(
            Escuela_ID,
            self.fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO,
            self.fluidez_1__lista_de_cursos
        )

        total_alumnos_por_tipo_de_desempeño_por_curso = DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
            total_alumnos_por_tipo_de_desempeño_por_curso_df             
        )

        return total_alumnos_por_tipo_de_desempeño_por_curso 
        
    def _fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division(self,Escuela_ID):
        dict_desempeño_por_curso_y_division_Bar_ChartJS = {}
        dict_total_alumnos_por_tipo_de_desempeño_por_curso_división1_tabla = {}
        [dict_desempeño_por_curso_division,
         dict_total_alumnos_por_tipo_de_desempeño_por_curso_división] = desempeño_por_escuela_curso_y_division(
            Escuela_ID,
            self.fluidez_df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,
            self.fluidez_1__lista_de_cursos
        )
        for Curso in self.fluidez_1__lista_de_cursos:
            desempeño_por_curso_division_df = dict_desempeño_por_curso_division.get(Curso)
            dict_desempeño_por_curso_y_division_Bar_ChartJS[Curso] = DataFrameToCharJS.convertir_dataFrame_a_Bar_ChartJS(
                desempeño_por_curso_division_df
            )
            total_alumnos_por_tipo_de_desempeño_por_curso_división_df = dict_total_alumnos_por_tipo_de_desempeño_por_curso_división.get(Curso)
            dict_total_alumnos_por_tipo_de_desempeño_por_curso_división1_tabla[Curso] = DataFrameToTabla.convertir_dataFrame_a_Tabla_De_Datos(
                total_alumnos_por_tipo_de_desempeño_por_curso_división_df             
            )

        return dict_desempeño_por_curso_y_division_Bar_ChartJS
    
    """
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