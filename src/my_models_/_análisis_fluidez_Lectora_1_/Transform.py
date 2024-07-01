from src.abstract_model.AbstractTransform import AbstractTransform
import pandas as pd

class Transform(AbstractTransform):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def apply(self, *args, **kwargs):
        pass

    def map(self, *args, **kwargs):
        pass

    def applymap(self, *args, **kwargs):
        pass

    def astype(self, *args, **kwargs):
        pass

    def melt(self, *args, **kwargs):
        pass

    def resample(self, *args, **kwargs):
        pass

    def rolling(self, *args, **kwargs):
        pass

    def calcular_DESEMPEÑO_por_Alumno_ID(self):
        self.dataframe['DESEMPEÑO'] =   self.dataframe.apply(lambda row: self.determinar_desempeño_por_fila( row ), axis=1)
        # reordenar columnas..
        self.dataframe = self.dataframe.reindex(columns=[
            'DESEMPEÑO',
            'Alumno_ID',
            'Operativo',
            'CURSO_NORMALIZADO',
            'Curso',
            'División',
            'Ausente',
            'Cantidad_de_palabras',
            'Prosodia',
            'Incluido',
            'Turno',
            'Modalidad',
            'Nivel',
            'Gestión',
            'Supervisión',
            'Escuela_ID',
            'Departamento',
            'Localidad',
            'zona',
            'Regional',
            'ciclo_lectivo',
            'separador'])
        return self.dataframe


    def determinar_desempeño_por_fila(self, row):
        condiciones = {
            ('2°', 'Primario'): [(0, 15, 'Crítico'), (16, 45, 'Básico'), (46, 70, 'Medio'), (71, float('inf'), 'Avanzado')],
            ('3°', 'Primario'): [(0, 30, 'Crítico'), (31, 60, 'Básico'), (61, 90, 'Medio'), (91, float('inf'), 'Avanzado')],
            ('4°', 'Primario'): [(0, 45, 'Crítico'), (46, 75, 'Básico'), (76, 110, 'Medio'), (111, float('inf'), 'Avanzado')],
            ('5°', 'Primario'): [(0, 60, 'Crítico'), (61, 90, 'Básico'), (91, 125, 'Medio'), (126, float('inf'), 'Avanzado')],
            ('6°', 'Primario'): [(0, 75, 'Crítico'), (76, 105, 'Básico'), (106, 140, 'Medio'), (141, float('inf'), 'Avanzado')],
            ('7°', 'Primario'): [(0, 85, 'Crítico'), (86, 115, 'Básico'), (116, 155, 'Medio'), (156, float('inf'), 'Avanzado')],
            ('1°', 'Secundario Orientado'): [(0, 95, 'Crítico'), (96, 125, 'Básico'), (126, 165, 'Medio'), (166, float('inf'), 'Avanzado')],
            ('1°', 'Secundario Técnico'): [(0, 95, 'Crítico'), (96, 125, 'Básico'), (126, 165, 'Medio'), (166, float('inf'), 'Avanzado')],
            ('1º Bilingüe', 'Secundario Orientado'): [(0, 95, 'Crítico'), (96, 125, 'Básico'), (126, 165, 'Medio'), (166, float('inf'), 'Avanzado')],
            ('1º Bilingüe', 'Secundario Técnico'): [(0, 95, 'Crítico'), (96, 125, 'Básico'), (126, 165, 'Medio'), (166, float('inf'), 'Avanzado')],
            ('2°', 'Secundario Orientado'): [(0, 105, 'Crítico'), (106, 135, 'Básico'), (136, 170, 'Medio'), (171, float('inf'), 'Avanzado')],
            ('2°', 'Secundario Técnico'): [(0, 105, 'Crítico'), (106, 135, 'Básico'), (136, 170, 'Medio'), (171, float('inf'), 'Avanzado')],
            ('2º Bilingüe', 'Secundario Orientado'): [(0, 105, 'Crítico'), (106, 135, 'Básico'), (136, 170, 'Medio'), (171, float('inf'), 'Avanzado')],
            ('2º Bilingüe', 'Secundario Técnico'): [(0, 105, 'Crítico'), (106, 135, 'Básico'), (136, 170, 'Medio'), (171, float('inf'), 'Avanzado')],
            ('3°', 'Secundario Orientado'): [(0, 115, 'Crítico'), (116, 145, 'Básico'), (146, 175, 'Medio'), (176, float('inf'), 'Avanzado')],
            ('3°', 'Secundario Técnico'): [(0, 115, 'Crítico'), (116, 145, 'Básico'), (146, 175, 'Medio'), (176, float('inf'), 'Avanzado')],
            ('3º Bilingüe', 'Secundario Orientado'): [(0, 115, 'Crítico'), (116, 145, 'Básico'), (146, 175, 'Medio'), (176, float('inf'), 'Avanzado')],
            ('3º Bilingüe', 'Secundario Técnico'): [(0, 115, 'Crítico'), (116, 145, 'Básico'), (146, 175, 'Medio'), (176, float('inf'), 'Avanzado')],
            ('4°', 'Secundario Orientado'): [(0, 120, 'Crítico'), (121, 150, 'Básico'), (151, 180, 'Medio'), (181, float('inf'), 'Avanzado')],
            ('4°', 'Secundario Técnico'): [(0, 120, 'Crítico'), (121, 150, 'Básico'), (151, 180, 'Medio'), (181, float('inf'), 'Avanzado')],
            ('4º Bilingüe', 'Secundario Orientado'): [(0, 120, 'Crítico'), (121, 150, 'Básico'), (151, 180, 'Medio'), (181, float('inf'), 'Avanzado')],
            ('4º Bilingüe', 'Secundario Técnico'): [(0, 120, 'Crítico'), (121, 150, 'Básico'), (151, 180, 'Medio'), (181, float('inf'), 'Avanzado')],
            ('5°', 'Secundario Orientado'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
            ('5°', 'Secundario Técnico'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
            ('5º Bilingüe', 'Secundario Orientado'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
            ('5º Bilingüe', 'Secundario Técnico'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
            ('6°', 'Secundario Orientado'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
            ('6°', 'Secundario Técnico'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
            ('6º Bilingüe', 'Secundario Orientado'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
            ('6º Bilingüe', 'Secundario Técnico'): [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (186, float('inf'), 'Avanzado')],
        }

        key = (row['CURSO_NORMALIZADO'], row['Nivel'])
        if key in condiciones:
            for min_val, max_val, desempeño in condiciones[key]:
                if min_val <= row['Cantidad_de_palabras'] <= max_val:
                    return desempeño
        return None  # or some default value if no condition matches

    
    def calcular_desempeño(self,listaDeColumnas, dF_dataFrameIzquierdo, dF_dataFrameDerecha, ColumnaY, ColumnaX, col_titulo):    
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