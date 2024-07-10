from src.my_models_._abstract_model_.AbstractGroupAggregation import AbstractGroupAggregation
import pandas as pd
import src.tools.utils as u
import os
import src.tools.DataFrameToTabla as dfToTable

from src.tools.generator_groups import generate_group_aggregation_class
from src.my_models_.___Filtros.PorEscuela.por_escuela import filtrar_datos_institucionales_por_escuela,filtrar_matricula_por_escuela,lista_de_cursos_escuela
from src.my_models_.___Filtros.PorEscuela.por_escuela_y_curso import filtrar_matricula_por_escuela_y_curso
from src.my_models_.___Filtros.PorEscuela.por_escuela_curso_y_división import filtrar_matricula_por_escuela_curso_y_division

class GroupAggregation(AbstractGroupAggregation):
    def __init__(self, processed_dataframe: pd.DataFrame):
        super().__init__(processed_dataframe)
        # generando los grupos que serán comunes a ambos dataframes
        # group_params_list = [
        #     (['Escuela_ID'],{'Alumno_ID': 'count'},{'reset_index': True}),
        #     (['Escuela_ID', 'CURSO_NORMALIZADO'],{'Alumno_ID': 'count'},{'reset_index': True}),
        #     (['Escuela_ID','CURSO_NORMALIZADO','División'],{'Alumno_ID': 'count'},{'reset_index': True}),
            
        #     (['Nivel_Unificado','CURSO_NORMALIZADO'],{'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Supervisión','CURSO_NORMALIZADO'],{'Alumno_ID':'count'}, {'reset_index': True}),

        # ]
        # generate_group_aggregation_class(group_params_list , os.path.dirname(os.path.abspath(__file__)),'GroupAggregationNominal')
        print('agrupando nominal')
        self.groupby()

    def agg(self, *args, **kwargs):
        pass

    def pivot_table(self, *args, **kwargs):
        pass

    def groupby(self, *args, **kwargs):        
        # agrupamientos que salen de la clase abstracta dado que son comunes para los dos dataframes
        self._df_Escuela_ID_Alumno_ID_count = self.df_Escuela_ID_Alumno_ID_count()
        self._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count()
        self._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count()
        self._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count()
        self._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count()
        # guardar los data frames
        self.salvar_df() 
        pass

    def salvar_df(self):
        u.save_dataframe_to_csv(self._df_Escuela_ID_Alumno_ID_count,'data/processed/transformed/Nominal/_df_FL_Escuela_ID_Alumno_ID_count.csv')
        u.save_dataframe_to_csv(self._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/Nominal/_df_FL_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,'data/processed/transformed/Nominal/_df_FL_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/Nominal/_df_FL_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/Nominal/_df_FL_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count.csv') 

    def datos_institucionales(self,Escuela_ID):
        datosInstitucionales_dict = filtrar_datos_institucionales_por_escuela(
            Escuela_ID,
            self.processed_dataframe            
        )
        return datosInstitucionales_dict
    
    def lista_de_cursos_escuela(self,Escuela_ID):
        lista_de_cursos = lista_de_cursos_escuela(
            Escuela_ID,
            self.processed_dataframe                        
        )        
        return lista_de_cursos
        
    def matricula_por_escuela(self,Escuela_ID):        
        return filtrar_matricula_por_escuela(
            Escuela_ID,
            self.processed_dataframe,
        )
    
    def matricula_por_curso(self,Escuela_ID):
        matricula_por_curso_df = filtrar_matricula_por_escuela_y_curso(            
            Escuela_ID,
            self._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count
        )
        return dfToTable.convertir_dataFrame_a_Tabla_De_Datos(
            matricula_por_curso_df
        )
    
    def matricula_por_curso_división(self,Escuela_ID):
        matricula_por_curso_división_tabla = {}
        dict_matricula_por_curso_division = filtrar_matricula_por_escuela_curso_y_division(
            Escuela_ID,
            self._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,            
            self.lista_de_cursos_escuela(Escuela_ID)
        )
        for Curso in self.lista_de_cursos_escuela(Escuela_ID):
            # saco el dataframe qu está dentro del diccionario
            matricula_por_curso_división_tabla[Curso] = dfToTable.convertir_dataFrame_a_Tabla_De_Datos(
                dict_matricula_por_curso_division.get(Curso))
            
        return matricula_por_curso_división_tabla
    


