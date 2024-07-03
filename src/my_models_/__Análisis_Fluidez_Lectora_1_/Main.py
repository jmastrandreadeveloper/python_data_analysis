### Análisis Fluiidez Lectora 1
import pandas as pd
from src.my_models_._abstract_model_.AbstractMain import AbstractMain
from .GroupAggregation import GroupAggregation
from .Preprocessor import Preprocessor
from .Transform import Transform
from .CalculadorDePorcentajes import CalculadorDePorcentajes

class Main(AbstractMain):

    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
        self.group_agg = GroupAggregation(dataframe)
        self.preprocessor = Preprocessor(dataframe)
        self.transform = Transform(dataframe)
        # acá empiezo con la ejecución 
        self.run_all()

    # análisis de fluidez lectora
    def run_all(self):
        # Implementar una secuencia de operaciones que utilicen los métodos de las instancias
        self.preprocessor.agregar_columna_Nivel_Unificado()
        #         
        # calcular desempeño por alumno, crear columna DESEMPEÑO
        self.transform.calcular_DESEMPEÑO_por_Alumno_ID()
        # agrupar dataframe por criterios
        #
        self.group_agg.groupby()

        # filtrar el dataframe para su análisis
        # alumnos incluidos = Si
        self.df_alumnos_incluidos_SI = self.preprocessor.filtrar_por_columna('Incluido','Si')
        # alumnos incluidos = No
        self.df_alumnos_incluidos_NO = self.preprocessor.filtrar_por_columna('Incluido','No')
        # seguir filtrando porque el dataframe debe ser filtrado por otras condiciones 
        # antes de empezar con los agrupamientos dado que necesitamos que queden aquellos
        # alumnos que cumplan con las condiciones










        # agregar columna Nivel_Unificado    
        self.preprocessor.agregar_columna_Nivel_Unificado()               
        # reordenar columnas
        self.dataframe = self.preprocessor.reordenar_columnas(
            [
                'Alumno_ID','DESEMPEÑO','Operativo','CURSO_NORMALIZADO','Curso','División','Ausente','Cantidad_de_palabras','Prosodia','Incluido','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','Regional','ciclo_lectivo','separador']
        )
        print(self.dataframe.columns)
        # calcular el porcentaje de desempeño de acuerdo a diferentes criterios
        # creo un objeto para tal fin
        self.calculador = CalculadorDePorcentajes(self.group_agg)
        self.calculador.calcular_porcentajes_desempeño()

        print(self.calculador.df_Desempeño_por_Escuela)
        print(self.calculador.df_Desempeño_por_Escuela_CURSO_NORMALIZADO)
        print(self.calculador.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division)
        print(self.calculador.df_Desempeño_por_Supervisión_CURSO_NORMALIZADO)
        print(self.calculador.df_Desempeño_por_Nivel_CURSO_NORMALIZADO)



        pass