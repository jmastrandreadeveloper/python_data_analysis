
import pandas as pd
from src.my_models_._abstract_model_.AbstractMain import AbstractMain
from .GroupAggregation import GroupAggregation
from .Preprocessor import Preprocessor
from .Transform import Transform
#$from .Report import Report
import src.utils as u

class Main(AbstractMain):

    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)        
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
        self.listaEscuelas_IDs = self.preprocessor.obtener_datos_de_columna('Escuela_ID' , True)
        # agregar columna Nivel_Unificado    
        self.dataframe = self.preprocessor.agregar_columna_Nivel_Unificado()
        # reordenar columnas
        self.dataframe = self.preprocessor.reordenar_columnas(
            self.dataframe,
            [
                'ciclo_lectivo','Alumno_ID','Sexo','Edad','Edad_Correcta','CURSO_NORMALIZADO','Curso','División','Turno','Modalidad','Nivel','Nivel_Unificado','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','AMBITO','Regional']
        )
        self.group_agg = GroupAggregation(self.dataframe)
        self.Nominal = self.dataframe
        #self.reporte()
        pass

    # def reporte(self):
    #     print('haciendo reporte del Nominal')
    #     # le paso el output path que en este caso no es nada - y además le paso la lista de las escuelas y el dataframe para que lo pueda trabajar
    #     #self.reporteNominal = Report('-',self.listaEscuelas_IDs,self.dataframe).do_report()
    #     self.datos_institucionales = filtrar_por_escuela
    #     self.datos_institucionales = None
    #     self.lista_de_cursos_escuela = None
    #     self.matricula_por_escuela = None
    #     self.matricula_por_curso = None
    #     self.matricula_por_curso_división = None
    #     self.fluidez_lectora_1 = None