from src.my_models_._abstract_model_.AbstractGroupAggregation import AbstractGroupAggregation
import pandas as pd
import src.tools.utils as u
import os
from src.tools.generator_groups import generate_group_aggregation_class

# acá importo la clase con el agrupamiento que voy a querer
#from src.my_models_.__Análisis_Fluidez_Lectora_1_.GroupAggregationFluidezLectora1 import GroupAggregationFLectora1
from src.my_models_.__Análisis_Fluidez_Lectora_1_.GroupAggregationFLectora1 import GroupAggregationFLectora1
from src.my_models_.___Filtros.PorEscuela.por_escuela import filtrar_matricula_por_escuela

class GroupAggregation(AbstractGroupAggregation):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)        
        ### 1 -autogenero los grupos para fluidez        
        # group_params_list = [
        #     (['Escuela_ID','DESEMPEÑO'],{'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Escuela_ID','CURSO_NORMALIZADO','DESEMPEÑO'], {'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Escuela_ID','CURSO_NORMALIZADO','División','DESEMPEÑO'],{'Alumno_ID':'count'},{'reset_index': True}),

        #     (['Nivel_Unificado','CURSO_NORMALIZADO','DESEMPEÑO'],{'Alumno_ID':'count'},{'reset_index': True}),
        #     (['Supervisión','CURSO_NORMALIZADO','DESEMPEÑO'],{'Alumno_ID':'count'}, {'reset_index': True}),
        # ]
        # generate_group_aggregation_class(group_params_list , os.path.dirname(os.path.abspath(__file__)),'GroupAggregationFLectora1')
        
        # acá voy a usar un tipo de agrupamiento que debo armar previamente
        self.group_agg_fl_1 = GroupAggregationFLectora1(self.processed_dataframe)

    def groupby(self, dataframe: pd.DataFrame):
        # llamo desde acá al agrupamiento que quiero..
        self.df_alumnos_con_MÁXIMA_cant_palabras = dataframe
        # agrupamientos que salen de la clase abstracta dado que son comunes para los dos dataframes
        self._df_Escuela_ID_Alumno_ID_count = self.df_Escuela_ID_Alumno_ID_count()
        self._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count()
        self._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count = self.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count()
        self._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count()
        self._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count = self.df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count()        
        # agrupamiento que son propios de este dataframe de fluidez lectora, estos agruipamientos están
        # en esta función., más abajo , son los que agrupan el desempeño y nos va a servir para poder
        # sacar los pocentajes de desempeño
        self._df_Escuela_ID_DESEMPEÑO_Alumno_ID_count = self.group_agg_fl_1.df_Escuela_ID_DESEMPEÑO_Alumno_ID_count()        
        self._df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count = self.group_agg_fl_1.df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count()        
        self._df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count = self.group_agg_fl_1.df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count()
        self._df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count = self.group_agg_fl_1.df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count()
        self._df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count = self.group_agg_fl_1.df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count()
        # guardar los data frames
        self.salvar_df()        

        return

    def agg(self, *args, **kwargs):
        pass

    def pivot_table(self, *args, **kwargs):
        pass       
        
    def salvar_df(self):
        u.save_dataframe_to_csv(self._df_Escuela_ID_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Escuela_ID_Alumno_ID_count.csv')
        u.save_dataframe_to_csv(self._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count.csv') 

        u.save_dataframe_to_csv(self._df_Escuela_ID_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Escuela_ID_DESEMPEÑO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count.csv') 
        u.save_dataframe_to_csv(self._df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/Fluidez_1/_df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count.csv') 

    def matricula_por_escuela_fluidez_lectora_1(self,Escuela_ID):
        return filtrar_matricula_por_escuela(
            Escuela_ID,
            self._df_Escuela_ID_Alumno_ID_count,
        ) 