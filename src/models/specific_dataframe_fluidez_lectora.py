import pandas as pd
from .abstract_dataframe import AbstractDataFrame

class SpecificDataFrameFluidezLectora(AbstractDataFrame):  
    
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)        
        self.transform_data()
        self.group_data()
        self.clean_data()
    
    def transform_data(self):
        self.calcular_desempeño_por_alumno()
        self.reordenar_columnas()
    
    def calcular_desempeño_por_alumno(self):
        self.dataframe['DESEMPEÑO'] = self.dataframe.apply(self.determinar_desempeño_por_fila, axis=1)

    def determinar_desempeño_por_fila(self, row):
        criterios = {
            'Primario': {
                '2°': [(0, 15, 'Crítico'), (16, 45, 'Básico'), (46, 70, 'Medio'), (70, float('inf'), 'Avanzado')],
                '3°': [(0, 30, 'Crítico'), (31, 60, 'Básico'), (61, 90, 'Medio'), (90, float('inf'), 'Avanzado')],
                '4°': [(0, 45, 'Crítico'), (46, 75, 'Básico'), (76, 110, 'Medio'), (110, float('inf'), 'Avanzado')],
                '5°': [(0, 60, 'Crítico'), (61, 90, 'Básico'), (91, 125, 'Medio'), (125, float('inf'), 'Avanzado')],
                '6°': [(0, 75, 'Crítico'), (76, 105, 'Básico'), (106, 140, 'Medio'), (140, float('inf'), 'Avanzado')],
                '7°': [(0, 85, 'Crítico'), (86, 115, 'Básico'), (116, 155, 'Medio'), (155, float('inf'), 'Avanzado')]
            },
            'Secundario Orientado': {
                '1°': [(0, 95, 'Crítico'), (96, 125, 'Básico'), (126, 165, 'Medio'), (165, float('inf'), 'Avanzado')],
                '2°': [(0, 105, 'Crítico'), (106, 135, 'Básico'), (136, 170, 'Medio'), (170, float('inf'), 'Avanzado')],
                '3°': [(0, 115, 'Crítico'), (116, 145, 'Básico'), (146, 175, 'Medio'), (175, float('inf'), 'Avanzado')],
                '4°': [(0, 120, 'Crítico'), (121, 150, 'Básico'), (151, 180, 'Medio'), (180, float('inf'), 'Avanzado')],
                '5°': [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (185, float('inf'), 'Avanzado')],
                '6°': [(0, 125, 'Crítico'), (126, 155, 'Básico'), (156, 185, 'Medio'), (185, float('inf'), 'Avanzado')]
            }
        }
        curso = row['CURSO_NORMALIZADO']
        nivel = row['Nivel']
        palabras = row['Cantidad_de_palabras']
        
        if nivel in criterios and curso in criterios[nivel]:
            for min_val, max_val, desempeño in criterios[nivel][curso]:
                if min_val <= palabras <= max_val:
                    return desempeño
        return 'Desconocido'  # Caso por defecto si no se encuentra un criterio coincidente
    
    def reordenar_columnas(self):
        columnas_ordenadas = [
            'DESEMPEÑO', 'Alumno_ID', 'Operativo', 'CURSO_NORMALIZADO', 'Curso', 'División', 'Ausente',
            'Cantidad_de_palabras', 'Prosodia', 'Incluido', 'Turno', 'Modalidad', 'Nivel', 'Gestión',
            'Supervisión', 'Escuela_ID', 'Departamento', 'Localidad', 'zona', 'Regional', 'ciclo_lectivo', 'separador'
        ]
        self.dataframe = self.dataframe.reindex(columns=columnas_ordenadas)
    
    def group_data(self):
        self.df_Desempeño_por_Escuela = self.calcular_desempeño(
            ['Escuela_ID'],
            self.agrupar_por_criterio(self.dataframe , ['Escuela_ID'], {'Alumno_ID': 'count'} , True),
            self.agrupar_por_criterio(self.dataframe , ['Escuela_ID', 'DESEMPEÑO'], {'Alumno_ID': 'count'} , True),
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Escuela_ID',    
            'Desempeño_por_Escuela'
        )
        
        self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO = self.calcular_desempeño(
            ['Escuela_ID', 'CURSO_NORMALIZADO'],
            self.agrupar_por_criterio(self.dataframe , ['Escuela_ID', 'CURSO_NORMALIZADO'], {'Alumno_ID': 'count'} , True),
            self.agrupar_por_criterio(self.dataframe , ['Escuela_ID', 'CURSO_NORMALIZADO', 'DESEMPEÑO'], {'Alumno_ID': 'count'} , True),
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Escuela_ID_y_CURSO_NORMALIZADO',    
            'Desempeño_por_Escuela_CURSO_NORMALIZADO'
        )

        self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division = self.calcular_desempeño(
            ['Escuela_ID','CURSO_NORMALIZADO','División'],
            self.agrupar_por_criterio(self.dataframe , ['Escuela_ID','CURSO_NORMALIZADO','División'], {'Alumno_ID':'count'} , True),
            self.agrupar_por_criterio(self.dataframe , ['Escuela_ID','CURSO_NORMALIZADO','División','DESEMPEÑO'],{'Alumno_ID':'count'}, True),
            'Total_Alumnos_por_Tipo_de_Desempeño',
            'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División',    
            'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'
        )
    
    def clean_data(self):
        self.df_Desempeño_por_Escuela['Total_Alumnos_por_Tipo_de_Desempeño'] = self.df_Desempeño_por_Escuela[
            'Total_Alumnos_por_Tipo_de_Desempeño'].astype(int).round(0)
        self.df_Desempeño_por_Escuela['Desempeño_por_Escuela'] = self.df_Desempeño_por_Escuela[
            'Desempeño_por_Escuela'].round(2).fillna(0)
        self.df_Desempeño_por_Escuela['Total_Alumnos_por_Escuela_ID'] = self.df_Desempeño_por_Escuela[
            'Total_Alumnos_por_Escuela_ID'].astype(int).round(0).fillna(0)
        
        # acá faltan más lineas
        self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO['Total_Alumnos_por_Tipo_de_Desempeño'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
            'Total_Alumnos_por_Tipo_de_Desempeño'].astype(int).round(0)
        

        # convierto en int la columna Total_Alumnos_por_Tipo_de_Desempeño
        self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
                'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'].astype(int).round(0)
        # reducir la cantidad de decimales
        self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
                'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'].round(2)
        self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
                'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División'].fillna(0)
        self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
            'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division[
                'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'].fillna(0)


# import pandas as pd
# from .abstract_dataframe import AbstractDataFrame

# class SpecificDataFrameFluidezLectora(AbstractDataFrame):  
    
#     def __init__(self, dataframe: pd.DataFrame):
#         super().__init__(dataframe)        
#         self.transform_data(self)
#         self.group_data(self)
#         self.clean_data(self)
    
#     def transform_data(self):
#         calcular_desempeño_por_alumno()
#         def calcular_desempeño_por_alumno():
#             self.dataframe['DESEMPEÑO'] =   self.dataframe.apply(lambda row: determinar_desempeño_por_fila( row ), axis=1)
#             # reordenar columnas..
#             self.dataframe = self.dataframe.reindex(columns=[
#                 'DESEMPEÑO',
#                 'Alumno_ID',
#                 'Operativo',
#                 'CURSO_NORMALIZADO',
#                 'Curso',
#                 'División',
#                 'Ausente',
#                 'Cantidad_de_palabras',
#                 'Prosodia',
#                 'Incluido',
#                 'Turno',
#                 'Modalidad',
#                 'Nivel',
#                 'Gestión',
#                 'Supervisión',
#                 'Escuela_ID',
#                 'Departamento',
#                 'Localidad',
#                 'zona',
#                 'Regional',
#                 'ciclo_lectivo',
#                 'separador'])
#             return

#         def determinar_desempeño_por_fila(row):
#             ## GRADO 2 PRIMARIA - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 15) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Crítico'
#             ## GRADO 2 PRIMARIA - NIVEL BÁSICO
#             if (row['Cantidad_de_palabras'] >= 16 and row['Cantidad_de_palabras'] <= 45) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Básico'	
#             ## GRADO 2 PRIMARIA - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 46 and row['Cantidad_de_palabras'] <= 70) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Medio'		
#             ## GRADO 2 PRIMARIA - NIVEL AVANZADO
#             if (row['Cantidad_de_palabras'] > 70 ) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Avanzado'
#             ## ################################-	
            
#             ## GRADO 3 PRIMARIA - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 30) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Crítico'
#             ## GRADO 3 PRIMARIA - NIVEL BÁSICO
#             if (row['Cantidad_de_palabras'] >= 31 and row['Cantidad_de_palabras'] <= 60) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Básico'	
#             ## GRADO 3 PRIMARIA - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 61 and row['Cantidad_de_palabras'] <= 90) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Medio'		
#             ## GRADO 3 PRIMARIA - NIVEL AVANZADO
#             if (row['Cantidad_de_palabras'] > 90 ) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Avanzado'
#             ## ################################-		
                
#             ## GRADO 4 PRIMARIA - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 45) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Crítico'
#             ## GRADO 4 PRIMARIA - NIVEL BÁSICO
#             if (row['Cantidad_de_palabras'] >= 46 and row['Cantidad_de_palabras'] <= 75) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Básico'	
#             ## GRADO 4 PRIMARIA - NIVEL AVANZADO 
#             if (row['Cantidad_de_palabras'] >= 76 and row['Cantidad_de_palabras'] <= 110) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Medio'		
#             ## GRADO 3 PRIMARIA - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] > 110 ) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Avanzado'	
#             ## ################################-
                
#             ## GRADO 5 PRIMARIA - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 60) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Crítico'
#             ## GRADO 5 PRIMARIA - NIVEL BÁSICO
#             if (row['Cantidad_de_palabras'] >= 61 and row['Cantidad_de_palabras'] <= 90) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Básico'	
#             ## GRADO 5 PRIMARIA - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 91 and row['Cantidad_de_palabras'] <= 125) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Medio'
#             ## GRADO 5 PRIMARIA - NIVEL AVANZADO
#             if (row['Cantidad_de_palabras'] > 125 ) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Avanzado'	
#             ## ################################-
            
#             ## GRADO 6 PRIMARIA - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 75) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Crítico'
#             ## GRADO 6 PRIMARIA - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 76 and row['Cantidad_de_palabras'] <= 105) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Básico'	
#             ## GRADO 6 PRIMARIA - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 106 and row['Cantidad_de_palabras'] <= 140) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Medio'
#             ## GRADO 6 PRIMARIA - NIVEL AVANZADO
#             if (row['Cantidad_de_palabras'] > 140 ) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Avanzado'	
#             ## ################################-
                
#             ## GRADO 7 PRIMARIA - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 85) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Crítico'
#             ## GRADO 7 PRIMARIA - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 86 and row['Cantidad_de_palabras'] <= 115) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Básico'	
#             ## GRADO 7 PRIMARIA - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 116 and row['Cantidad_de_palabras'] <= 155) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Medio'
#             ## GRADO 7 PRIMARIA - NIVEL AVANZADO	
#             if (row['Cantidad_de_palabras'] > 155 ) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Avanzado'
#             ## ################################-
                
#             ## CURSO 1 SECUNDARIAS - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 95) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
#             ## CURSO 1 SECUNDARIAS - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 96 and row['Cantidad_de_palabras'] <= 125) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
#             ## CURSO 1 SECUNDARIAS - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 126 and row['Cantidad_de_palabras'] <= 165) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
#             ## CURSO 1 SECUNDARIAS - NIVEL AVANZADO	
#             if (row['Cantidad_de_palabras'] > 165 ) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
#             ## ################################-
                
#             ## CURSO 2 SECUNDARIAS - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 105) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
#             ## CURSO 2 SECUNDARIAS - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 106 and row['Cantidad_de_palabras'] <= 135) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
#             ## CURSO 2 SECUNDARIAS - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 136 and row['Cantidad_de_palabras'] <= 170) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
#             ## CURSO 2 SECUNDARIAS - NIVEL AVANZADO	
#             if (row['Cantidad_de_palabras'] > 170 ) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
#             ## ################################-
                
#             ## CURSO 3 SECUNDARIAS - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 115) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
#             ## CURSO 3 SECUNDARIAS - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 116 and row['Cantidad_de_palabras'] <= 145) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
#             ## CURSO 3 SECUNDARIAS - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 146 and row['Cantidad_de_palabras'] <= 175) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
#             ## CURSO 3 SECUNDARIAS - NIVEL AVANZADO	
#             if (row['Cantidad_de_palabras'] > 175 ) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
#             ## ################################-
                
#             ## CURSO 4 SECUNDARIAS - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 120) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
#             ## CURSO 4 SECUNDARIAS - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 121 and row['Cantidad_de_palabras'] <= 150) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
#             ## CURSO 4 SECUNDARIAS - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 151 and row['Cantidad_de_palabras'] <= 180) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
#             ## CURSO 4 SECUNDARIAS - NIVEL AVANZADO	
#             if (row['Cantidad_de_palabras'] > 180 ) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
#             ## ################################-
                
#             ## CURSO 5 SECUNDARIAS - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 125) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
#             ## CURSO 5 SECUNDARIAS - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 126 and row['Cantidad_de_palabras'] <= 155) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
#             ## CURSO 5 SECUNDARIAS - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 156 and row['Cantidad_de_palabras'] <= 185) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
#             ## CURSO 5 SECUNDARIAS - NIVEL AVANZADO	
#             if (row['Cantidad_de_palabras'] > 185 ) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
#             ## ################################-
                
#             ## CURSO 6 SECUNDARIAS - NIVEL CRÍTICO
#             if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 125) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
#             ## CURSO 6 SECUNDARIAS - NIVEL BÁSICO	
#             if (row['Cantidad_de_palabras'] >= 126 and row['Cantidad_de_palabras'] <= 155) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
#             ## CURSO 6 SECUNDARIAS - NIVEL MEDIO 
#             if (row['Cantidad_de_palabras'] >= 156 and row['Cantidad_de_palabras'] <= 185) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
#             ## CURSO 6 SECUNDARIAS - NIVEL AVANZADO	
#             if (row['Cantidad_de_palabras'] > 185 ) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
#             ## ################################-
#             return
        
    
#     def group_data(self):
#         #########################################################################################################
#         self.df_Desempeño_por_Escuela = super().calcular_desempeño(self,
#             ['Escuela_ID'],
#             super().agrupar_por_criterio(self,
#                 self.dataframe,
#                 ['Escuela_ID'],
#                 {'Alumno_ID':'count'},
#                 True
#             ),
#             super().agrupar_por_criterio(self,
#                 self.dataframe,
#                 ['Escuela_ID','DESEMPEÑO'],
#                 {'Alumno_ID':'count'},
#                 True
#             ),
#             'Total_Alumnos_por_Tipo_de_Desempeño',
#             'Total_Alumnos_por_Escuela_ID',    
#             'Desempeño_por_Escuela'
#         )
#         #########################################################################################################
#         self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO = super().calcular_desempeño(self,
#             ['Escuela_ID','CURSO_NORMALIZADO'],
#             super().agrupar_por_criterio(self,
#                 self.dataframe,
#                 ['Escuela_ID','CURSO_NORMALIZADO'],
#                 {'Alumno_ID':'count'},
#                 True
#             ),
#             super().agrupar_por_criterio(self,
#                 self.dataframe,
#                 ['Escuela_ID','CURSO_NORMALIZADO','DESEMPEÑO'],
#                 {'Alumno_ID':'count'},
#                 True
#             ),
#             'Total_Alumnos_por_Tipo_de_Desempeño',
#             'Total_Alumnos_por_Escuela_ID_y_CURSO_NORMALIZADO',    
#             'Desempeño_por_Escuela_CURSO_NORMALIZADO'
#         )
#         #########################################################################################################
#         return
    
#     def clean_data(self):
#         # convierto en int la columna Total_Alumnos_por_Tipo_de_Desempeño
#         self.df_Desempeño_por_Escuela[
#             'Total_Alumnos_por_Tipo_de_Desempeño'] = self.df_Desempeño_por_Escuela[
#                 'Total_Alumnos_por_Tipo_de_Desempeño'].astype(int).round(0)
#         # reducir la cantidad de decimales
#         self.df_Desempeño_por_Escuela[
#             'Desempeño_por_Escuela'] = self.df_Desempeño_por_Escuela[
#                 'Desempeño_por_Escuela'].round(2)
#         self.df_Desempeño_por_Escuela[
#             'Total_Alumnos_por_Tipo_de_Desempeño'] = self.df_Desempeño_por_Escuela[
#                 'Total_Alumnos_por_Tipo_de_Desempeño'].fillna(0)
#         self.df_Desempeño_por_Escuela[
#             'Desempeño_por_Escuela'] = self.df_Desempeño_por_Escuela[
#                 'Desempeño_por_Escuela'].fillna(0)
#         self.df_Desempeño_por_Escuela[
#             'Total_Alumnos_por_Escuela_ID'] = self.df_Desempeño_por_Escuela[
#                 'Total_Alumnos_por_Escuela_ID'].astype(int).round(0)
#         self.df_Desempeño_por_Escuela[
#             'Total_Alumnos_por_Escuela_ID'] = self.df_Desempeño_por_Escuela[
#                 'Total_Alumnos_por_Escuela_ID'].fillna(0)
#         ########################################################################
#         # convierto en int la columna Total_Alumnos_por_Tipo_de_Desempeño
#         self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#             'Total_Alumnos_por_Tipo_de_Desempeño'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#                 'Total_Alumnos_por_Tipo_de_Desempeño'].astype(int).round(0)
#         # reducir la cantidad de decimales
#         self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#             'Desempeño_por_Escuela_CURSO_NORMALIZADO'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#                 'Desempeño_por_Escuela_CURSO_NORMALIZADO'].round(2)
#         self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#             'Total_Alumnos_por_Tipo_de_Desempeño'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#                 'Total_Alumnos_por_Tipo_de_Desempeño'].fillna(0)
#         self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#             'Desempeño_por_Escuela_CURSO_NORMALIZADO'] = self.df_Desempeño_por_Escuela_CURSO_NORMALIZADO[
#                 'Desempeño_por_Escuela_CURSO_NORMALIZADO'].fillna(0)
#         return

#     # def filter_data(self, column, value):
#     #     return self.dataframe[self.dataframe[column] == value]