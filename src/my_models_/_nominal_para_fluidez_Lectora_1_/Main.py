
import pandas as pd
import utils as u
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

    def run_all(self):
        # Implementar una secuencia de operaciones que utilicen los métodos de las instancias
        # dejar solamente las filas que necesitamos, estas son todas aquellas que sea CURSO_NORMALIZADO = 1°, 2°, 3°, 4°, 5°, 6°, 7°, 
        # dejar :  1°  2°  3°  4°  5°  6°  7°
        # eliminar : Múltiple Domiciliario -  Nivel I
        u.save_dataframe_to_csv(self.preprocessor.conservar_filas('CURSO_NORMALIZADO',['1°' , '2°' , '3°' , '4°' , '5°' , '6°' , '7°']),'data/processed/transformed/df_nominal_filas_conservadas.csv')
        # arreglar la columna edad para que queden todos en formato numérico
        self.preprocessor.fix_columna_edad()
        # obtener la lista de las escuelas a analizar buscando en la columna Escuela_ID y devolviendo una lista de ellas
        self.Escuelas_IDs = self.preprocessor.obtener_datos_de_columna('Escuela_ID' , True)
        # agregar columna Nivel_Unificado    
        self.preprocessor.agregar_columna_Nivel_Unificado()
        # reordenar columnas
        self.dataframe = self.preprocessor.reordenar_columnas(
            [
                'ciclo_lectivo','Alumno_ID','Sexo','Edad','Edad_Correcta','CURSO_NORMALIZADO','Curso','División','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','AMBITO','Regional']
        )
        print(self.dataframe.columns)
        pass