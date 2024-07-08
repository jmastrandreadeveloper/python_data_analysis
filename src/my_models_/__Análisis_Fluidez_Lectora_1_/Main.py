### Análisis Fluiidez Lectora 1
import pandas as pd
import src.utils as u
from src.my_models_._abstract_model_.AbstractMain import AbstractMain
from .GroupAggregation import GroupAggregation
from .Preprocessor import Preprocessor
from .Transform import Transform
#from .Report import Report
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
        # calcular desempeño por alumno, crear columna DESEMPEÑO
        self.dataframe = self.transform.calcular_DESEMPEÑO_por_Alumno_ID()
        self.dataframe = self.preprocessor.reordenar_columnas(
            self.dataframe,
            [
                'Alumno_ID','DESEMPEÑO','Operativo','CURSO_NORMALIZADO','Curso','División','Ausente','Cantidad_de_palabras','Prosodia','Incluido','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','Regional','ciclo_lectivo','separador']
        )
        u.save_dataframe_to_csv(self.dataframe,'data/processed/transformed/DESEMPEÑO_por alumno calculado en Main.csv')        
        
        # filtrar dataframe
        self.preprocessor.filtrar_dataframe(self.dataframe)
        # crear el objeto para agrupar el df de fluidez
        self.group_agg = GroupAggregation(self.preprocessor._df_alumnos_con_MÁXIMA_cant_palabras)
        # agrupar dataframe por criterios
        self.group_agg.groupby(self.preprocessor._df_alumnos_con_MÁXIMA_cant_palabras)        
        
        # calcular el porcentaje de desempeño de acuerdo a diferentes criterios
        # creo un objeto para tal fin
        self.calculador = CalculadorDePorcentajes(self.group_agg)
        self.calculador.calcular_porcentajes_desempeño()

        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Escuela,'data/processed/transformed/_df_Desempeño_por_Escuela.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Escuela_CURSO_NORMALIZADO,'data/processed/transformed/_df_Desempeño_por_Escuela_CURSO_NORMALIZADO.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,'data/processed/transformed/_df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,'data/processed/transformed/_df_Desempeño_por_Supervisión_CURSO_NORMALIZADO.csv') 
        u.save_dataframe_to_csv(self.calculador._df_Desempeño_por_Nivel_CURSO_NORMALIZADO,'data/processed/transformed/_df_Desempeño_por_Nivel_CURSO_NORMALIZADO.csv') 

        #self.reporte()

        pass

    # def reporte(self):
    #     print('haciendo reporte de Fluiez')
    #     self.reporteFluidez = Report('-')