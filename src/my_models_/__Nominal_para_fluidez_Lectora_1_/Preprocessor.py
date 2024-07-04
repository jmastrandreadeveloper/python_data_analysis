from src.my_models_._abstract_model_.AbstractPreprocessor import AbstractPreprocessor
import pandas as pd
import utils as u

class Preprocessor(AbstractPreprocessor):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def isnull(self, *args, **kwargs):
        pass

    def notnull(self, *args, **kwargs):
        pass

    def fillna(self, *args, **kwargs):
        pass

    def dropna(self, *args, **kwargs):
        pass

    def drop(self, *args, **kwargs):
        pass

    def rename(self, *args, **kwargs):
        pass

    def sort_values(self, *args, **kwargs):
        pass

    def sort_index(self, *args, **kwargs):
        pass

    ######################################### acá comienzo con mi código #################################
    def fix_columna_edad(self):
        print('...arreglando datos de la columna edad...')
        def create_age_reference() -> dict:
            """
            Crear un diccionario de referencia de edades.
            """
            age_reference = {
                ('Primario', '1°'): 6,
                ('Primario', '2°'): 7,
                ('Primario', '3°'): 8,
                ('Primario', '4°'): 9,
                ('Primario', '5°'): 10,
                ('Primario', '6°'): 11,
                ('Primario', '7°'): 12,

                ('Secundario Orientado', '1°'): 13,
                ('Secundario Orientado', '2°'): 14,
                ('Secundario Orientado', '3°'): 15,
                ('Secundario Orientado', '4°'): 16,
                ('Secundario Orientado', '5°'): 17,
                ('Secundario Orientado', '6°'): 18,

                ('Secundario Técnico', '1°'): 13,
                ('Secundario Técnico', '2°'): 14,
                ('Secundario Técnico', '3°'): 15,
                ('Secundario Técnico', '4°'): 16,
                ('Secundario Técnico', '5°'): 17,
                ('Secundario Técnico', '6°'): 18,
            }
            return age_reference
    
        
        def correct_invalid_ages(age_reference: dict) :
            """
            Corrige las edades inválidas utilizando la referencia de edades.
            """
            # Definir la función para obtener la edad correcta
            def get_correct_age(row, distancia):
                key = (row['Nivel'], row['Curso'])
                
                if key in age_reference:
                    reference_age = age_reference[key]
                    try:
                        current_age = int(row['Edad'])
                        if abs(current_age - reference_age) > distancia:
                            return reference_age
                        else:
                            return current_age
                    except ValueError:
                        # Si la edad no es un número válido, devolver la edad de referencia
                        return reference_age
                else:
                    try:
                        return int(row['Edad'])
                    except ValueError:
                        # Si la edad no es un número válido y no se encuentra la clave en el diccionario,
                        # se devuelve np.nan (o puedes devolver otro valor si lo prefieres)
                        return np.nan

            

            # esto significa que la diferencia entre la edad leída del df
            # y la que se toma como referencia no debe ser mayor a 2
            # sive para cuando tenemos un valor demasiado grande o muy chico
            # en alguno de esos casos debo poder resolverlo buscando su edad referencia
            distancia_entre_edades = 2

            # Corregir edades inválidas
            # if invalid_ages_mask.any():
            #     dataframe.loc[invalid_ages_mask, 'Edad'] = dataframe[invalid_ages_mask].apply(get_correct_age, axis=1, distancia=distancia_entre_edades)
            
            # Rastrear edades fuera del límite permitido y corregirlas
            # for (curso, nivel), edad in age_reference.items():
            #     mask = (dataframe['CURSO_NORMALIZADO'] == curso) & (dataframe['Nivel'] == nivel)
            #     dataframe.loc[mask & (dataframe['Edad'] > edad), 'Edad'] = edad
            self.dataframe['Edad_Correcta'] = self.dataframe.apply(get_correct_age, axis=1, distancia=distancia_entre_edades)
            # reordenar las columnas
            # reordenar columnas
            self.dataframe = self.reordenar_columnas(
                self.dataframe,
                [
                    'ciclo_lectivo','Alumno_ID','Sexo','Edad','Edad_Correcta','CURSO_NORMALIZADO','Curso','División','Turno','Modalidad','Nivel','Gestión','Supervisión','Escuela_ID','Departamento','Localidad','zona','AMBITO','Regional',]
            )
            return self.dataframe

        def validate_data():
            # Create age reference based on the dataframe
            age_reference = create_age_reference()
            # Correct invalid ages
            self.dataframe = correct_invalid_ages(age_reference)
            return self.dataframe
        
        validate_data()
        u.save_dataframe_to_csv(self.dataframe,'data/processed/transformed/df_nominal_con_edades_válidas.csv')
        return self.dataframe

