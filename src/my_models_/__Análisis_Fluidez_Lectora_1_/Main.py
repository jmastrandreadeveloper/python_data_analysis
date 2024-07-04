### Análisis Fluiidez Lectora 1
import pandas as pd
import utils as u
from src.my_models_._abstract_model_.AbstractMain import AbstractMain
from .GroupAggregation import GroupAggregation
from .Preprocessor import Preprocessor
from .Transform import Transform
from .Report import Report
from .CalculadorDePorcentajes import CalculadorDePorcentajes

class Main(AbstractMain):

    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)        
        self.preprocessor = Preprocessor(dataframe)
        self.transform = Transform(dataframe)
        # acá empiezo con la ejecución 
        self.run_all()

    # análisis de fluidez lectora
    def run_all(self):
        # Implementar una secuencia de operaciones que utilicen los métodos de las instancias
        # agregar columna Nivel_Unificado  
        self.dataframe = self.preprocessor.agregar_columna_Nivel_Unificado()
        # reordenar columnas
        self.dataframe = self.preprocessor.reordenar_columnas(
            self.dataframe,
            [
                'Alumno_ID','Operativo','CURSO_NORMALIZADO','Curso','División','Ausente','Cantidad_de_palabras','Prosodia','Incluido','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','Regional','ciclo_lectivo','separador']
        )
        print(self.dataframe.columns)
        
        # calcular desempeño por alumno, crear columna DESEMPEÑO
        self.dataframe = self.transform.calcular_DESEMPEÑO_por_Alumno_ID()
        self.dataframe = self.preprocessor.reordenar_columnas(
            self.dataframe,
            [
                'Alumno_ID','DESEMPEÑO','Operativo','CURSO_NORMALIZADO','Curso','División','Ausente','Cantidad_de_palabras','Prosodia','Incluido','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','Regional','ciclo_lectivo','separador']
        )
        u.save_dataframe_to_csv(self.dataframe,'data/processed/transformed/DESEMPEÑO_por alumno calculado en Main.csv')        
        
        # filtrar dataframe
        [df_alumnos_incluidos_SI,
         df_alumnos_incluidos_NO,
         df_alumnos_con_DESEMPEÑO,
         df_alumnos_sin_DESEMPEÑO,
         df_alumnos_menor_a_300_palabras,
         df_alumnos_mayor_a_300_palabras,
         df_alumnos_con_MÁXIMA_cant_palabras
        ] = self.preprocessor.filtrar_dataframe(self.dataframe)

        u.save_dataframe_to_csv(df_alumnos_con_MÁXIMA_cant_palabras,'data/processed/transformed/df_alumnos_con_MÁXIMA_cant_palabras.csv') 

        self.group_agg = GroupAggregation(df_alumnos_con_MÁXIMA_cant_palabras)
        # agrupar dataframe por criterios
        self.group_agg.groupby(df_alumnos_con_MÁXIMA_cant_palabras)

        u.save_dataframe_to_csv(self.group_agg._df_Escuela_ID_Alumno_ID_count,'data/processed/transformed/df_Escuela_ID_Alumno_ID_count_.csv')
        u.save_dataframe_to_csv(self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count_.csv') 
        u.save_dataframe_to_csv(self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,'data/processed/transformed/df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count_.csv') 
        u.save_dataframe_to_csv(self.group_agg._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count_.csv') 
        u.save_dataframe_to_csv(self.group_agg._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count,'data/processed/transformed/df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count_.csv') 

        u.save_dataframe_to_csv(self.group_agg._df_Escuela_ID_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/df_Escuela_ID_DESEMPEÑO_Alumno_ID_count_.csv') 
        u.save_dataframe_to_csv(self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count_.csv') 
        u.save_dataframe_to_csv(self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count_.csv') 
        u.save_dataframe_to_csv(self.group_agg._df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count_.csv') 
        u.save_dataframe_to_csv(self.group_agg._df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,'data/processed/transformed/df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count_.csv') 
        
        # calcular el porcentaje de desempeño de acuerdo a diferentes criterios
        # creo un objeto para tal fin
        self.calculador = CalculadorDePorcentajes(self.group_agg)
        self.calculador.calcular_porcentajes_desempeño()

        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Escuela,'data/processed/transformed/_df_Desempeño_por_Escuela.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Escuela_CURSO_NORMALIZADO,'data/processed/transformed/_df_Desempeño_por_Escuela_CURSO_NORMALIZADO.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,'data/processed/transformed/_df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,'data/processed/transformed/_df_Desempeño_por_Supervisión_CURSO_NORMALIZADO.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Nivel_CURSO_NORMALIZADO,'data/processed/transformed/_df_Desempeño_por_Nivel_CURSO_NORMALIZADO.csv') 

        reporte = Report('algo')
        reporte.do_report()



        pass
