import pandas as pd
import src.tools.utils as u
from src.my_models_.__Análisis_Fluidez_Lectora_1_.GroupAggregation import GroupAggregation
from src.my_models_.__Análisis_Fluidez_Lectora_1_.Preprocessor import Preprocessor
from src.tools.generator_filters import generate_filter_class

"""
Esta clase va a calcular los porcentajes de desempeño
va a recibir todos los dataframes para que haga los cálculos
"""
class CalculadorDePorcentajes:
    def __init__(self , group_agg : GroupAggregation):
        self.group_agg = group_agg
        self.preprocessor = Preprocessor(None)

        # probando filtros
        # Ejemplo de uso
        filter_methods = {
            'matricula_por_escuela': 'nominal_df_Escuela_ID_Alumno_ID_count',
            'desempeno_por_curso': 'nominal_df_Escuela_ID_Desempeno'
        }

        main_dir = ''
        filter_dir = '______Filtros'
        class_name = 'Filtro'

        generate_filter_class(filter_methods, main_dir, filter_dir, class_name)


        pass

    def calcular_porcentajes_desempeño(self):
        print('calculando porcentajes de desempeño')
        # porcentaje de desempeño por escuela
        self._df_Desempeño_por_Escuela = self.porcentajes_desempeño(
            ['Escuela_ID'],
            self.group_agg._df_Escuela_ID_Alumno_ID_count,
            self.group_agg._df_Escuela_ID_DESEMPEÑO_Alumno_ID_count,
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Escuela_ID',
            'Desempeño_por_Escuela'
        )
        # fix las columnas para que queden con valores enteros y los float con dos valores después del punto
        self._df_Desempeño_por_Escuela = self.preprocessor.clean_dataframe(
            self._df_Desempeño_por_Escuela,
            ['Total_Alumnos_por_Tipo_de_Desempeño','Total_Alumnos_por_Escuela_ID'],
            ['Desempeño_por_Escuela']
        )

        # porcentaje de desempeño por escuela y curso normalizado 
        self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO = self.porcentajes_desempeño(
            ['Escuela_ID','CURSO_NORMALIZADO'],
            self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count,
            self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Escuela_ID_y_CURSO_NORMALIZADO',
            'Desempeño_por_Escuela_CURSO_NORMALIZADO'
        )        
        self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO = self.preprocessor.clean_dataframe(
            self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO,
            ['Total_Alumnos_por_Tipo_de_Desempeño','Total_Alumnos_por_Escuela_ID_y_CURSO_NORMALIZADO'],
            ['Desempeño_por_Escuela_CURSO_NORMALIZADO']
        )

        # porcentaje de desempeño por escuela curso y división
        self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = self.porcentajes_desempeño(
            ['Escuela_ID','CURSO_NORMALIZADO','División'],
            self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count,
            self.group_agg._df_Escuela_ID_CURSO_NORMALIZADO_División_DESEMPEÑO_Alumno_ID_count,
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División',
            'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'
        )
        self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = self.preprocessor.clean_dataframe(
            self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,
            ['Total_Alumnos_por_Tipo_de_Desempeño','Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'],
            ['Desempeño_por_Escuela_CURSO_NORMALIZADO_Division']
        )
        # porcentaje de desempeño por supervisión y curso
        self._df_Desempeño_por_Supervisión_CURSO_NORMALIZADO = self.porcentajes_desempeño(
            ['Supervisión','CURSO_NORMALIZADO'],
            self.group_agg._df_Supervisión_CURSO_NORMALIZADO_Alumno_ID_count,
            self.group_agg._df_Supervisión_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Supervisión_CURSO_NORMALIZADO',
            'Desempeño_por_Supervisión_CURSO_NORMALIZADO'
        )
        self._df_Desempeño_por_Supervisión_CURSO_NORMALIZADO = self.preprocessor.clean_dataframe(
            self._df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,
            ['Total_Alumnos_por_Tipo_de_Desempeño','Total_Alumnos_por_Supervisión_CURSO_NORMALIZADO'],
            ['Desempeño_por_Supervisión_CURSO_NORMALIZADO']
        )
        # porcentaje de desempeño por nivel y curso
        self._df_Desempeño_por_Nivel_CURSO_NORMALIZADO = self._df_Desempeño_por_Nivel_CURSO_NORMALIZADO = self.porcentajes_desempeño(
            ['Nivel_Unificado','CURSO_NORMALIZADO'],
            self.group_agg._df_Nivel_Unificado_CURSO_NORMALIZADO_Alumno_ID_count,
            self.group_agg._df_Nivel_Unificado_CURSO_NORMALIZADO_DESEMPEÑO_Alumno_ID_count,
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Nivel_CURSO_NORMALIZADO',
            'Desempeño_por_Nivel_CURSO_NORMALIZADO'
        )
        self._df_Desempeño_por_Nivel_CURSO_NORMALIZADO = self.preprocessor.clean_dataframe(
            self._df_Desempeño_por_Nivel_CURSO_NORMALIZADO,
            ['Total_Alumnos_por_Tipo_de_Desempeño','Total_Alumnos_por_Nivel_CURSO_NORMALIZADO'],
            ['Desempeño_por_Nivel_CURSO_NORMALIZADO']
        )
        # guardar los data frames
        self.salvar_df()
        pass

    def porcentajes_desempeño(self,listaDeColumnas, dF_dataFrameIzquierdo, dF_dataFrameDerecha, ColumnaY, ColumnaX, col_titulo):    
        # Esta función calcula los porcentajes de desempeños de acuerdo a las columnas que se les pasa por parámetros.
        # La idea es que se puedan determinar por escuela, por curso, por división, etc., manteniendo la referencia de Alumno_ID
        # y renombrando las columnas de acuerdo a los parámetros suministrados.    
        # Realizando la fusión de los dataframes.
        dF_desempeño = pd.merge(dF_dataFrameIzquierdo, dF_dataFrameDerecha, how="left", on=listaDeColumnas)    
        # Renombrando las columnas 'Alumno_ID_x' y 'Alumno_ID_y' según los parámetros suministrados, asumiendo que ambas columnas contienen los mismos valores.
        # Esto implica que se puede mantener solo una de estas columnas para evitar duplicados.
        dF_desempeño.rename(columns={'Alumno_ID_x': ColumnaX, 'Alumno_ID_y': ColumnaY}, inplace=True)
        # Calculando el porcentaje de desempeño.
        dF_desempeño[col_titulo] = dF_desempeño[ColumnaY] / dF_desempeño[ColumnaX] * 100    
        # Opcional: Si se desea eliminar una de las columnas de Alumno_ID para evitar redundancia, puedes descomentar la siguiente línea:
        # dF_desempeño.drop(columns=[ColumnaY], inplace=True)
        return dF_desempeño
    
    def salvar_df(self):
        u.save_dataframe_to_csv(self._df_Desempeño_por_Escuela,'data/processed/transformed/Fluidez_1/_df_Desempeño_por_Escuela.csv')
        u.save_dataframe_to_csv(self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO,'data/processed/transformed/Fluidez_1/_df_Desempeño_por_Escuela_CURSO_NORMALIZADO.csv') 
        u.save_dataframe_to_csv(self._df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division,'data/processed/transformed/Fluidez_1/_df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division.csv') 
        u.save_dataframe_to_csv(self._df_Desempeño_por_Supervisión_CURSO_NORMALIZADO,'data/processed/transformed/Fluidez_1/_df_Desempeño_por_Supervisión_CURSO_NORMALIZADO.csv') 
        u.save_dataframe_to_csv(self._df_Desempeño_por_Nivel_CURSO_NORMALIZADO,'data/processed/transformed/Fluidez_1/_df_Desempeño_por_Nivel_CURSO_NORMALIZADO.csv')