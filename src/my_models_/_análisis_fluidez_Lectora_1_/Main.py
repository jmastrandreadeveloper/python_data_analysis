
import pandas as pd
import src.utils as u
from src.abstract_model.AbstractMain import AbstractMain
from .GroupAggregation import GroupAggregation
from .Preprocessor import Preprocessor
from .Transform import Transform

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
        #         
        # calcular desempeño por alumno, crear columna DESEMPEÑO
        self.transform.calcular_DESEMPEÑO_por_Alumno_ID()
        # agrupar dataframe por criterios
        #
        self.group_agg.groupby()
        print(self.group_agg.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count)

        

        # filtrar el dataframe para su análisis
        # alumnos incluidos = Si
        self.df_alumnos_incluidos_SI = self.preprocessor.filtrar_por_columna('Incluido','Si')
        # alumnos incluidos = No
        self.df_alumnos_incluidos_NO = self.preprocessor.filtrar_por_columna('Incluido','No')

        # agregar columna Nivel_Unificado    
        self.preprocessor.agregar_columna_Nivel_Unificado()               
        # reordenar columnas
        self.dataframe = self.preprocessor.reordenar_columnas(
            [
                'Alumno_ID','DESEMPEÑO','Operativo','CURSO_NORMALIZADO','Curso','División','Ausente','Cantidad_de_palabras','Prosodia','Incluido','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','Regional','ciclo_lectivo','separador']
        )
        print(self.dataframe.columns)
        # calcular el desempeño por alumno
        pass