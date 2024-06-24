 # Go to "Command Palette" Ctrl + Shift + P (View>Command Palette); Type in & select "Convert Indentation to Spaces" and press Enter. Share.


import sys
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería
import pandas       as pd


# determinar el desempeño por cada alumno, crear una columna calculada en base a la cantidad de palabras
# leidas, el curso y el nivel en el que está el alumno..
# se realiza a nivel de fila del dataframe
def calcular_desempeño_por_alumno(dataFrame):
     dataFrame['DESEMPEÑO'] =   dataFrame.apply(lambda row: determinar_desempeño_por_fila( row ), axis=1)
     # reordenar columnas..
     dataFrame = dataFrame.reindex(columns=[
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
     return dataFrame

def determinar_desempeño_por_fila(row):
    ## GRADO 2 PRIMARIA - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 15) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Crítico'
    ## GRADO 2 PRIMARIA - NIVEL BÁSICO
    if (row['Cantidad_de_palabras'] >= 16 and row['Cantidad_de_palabras'] <= 45) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Básico'	
    ## GRADO 2 PRIMARIA - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 46 and row['Cantidad_de_palabras'] <= 70) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Medio'		
    ## GRADO 2 PRIMARIA - NIVEL AVANZADO
    if (row['Cantidad_de_palabras'] > 70 ) and (row['CURSO_NORMALIZADO'] == '2°' and row['Nivel'] == 'Primario')  : return  'Avanzado'
    ## ################################-	
    
    ## GRADO 3 PRIMARIA - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 30) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Crítico'
    ## GRADO 3 PRIMARIA - NIVEL BÁSICO
    if (row['Cantidad_de_palabras'] >= 31 and row['Cantidad_de_palabras'] <= 60) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Básico'	
    ## GRADO 3 PRIMARIA - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 61 and row['Cantidad_de_palabras'] <= 90) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Medio'		
    ## GRADO 3 PRIMARIA - NIVEL AVANZADO
    if (row['Cantidad_de_palabras'] > 90 ) and (row['CURSO_NORMALIZADO'] == '3°' and row['Nivel'] == 'Primario')  : return  'Avanzado'
    ## ################################-		
        
    ## GRADO 4 PRIMARIA - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 45) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Crítico'
    ## GRADO 4 PRIMARIA - NIVEL BÁSICO
    if (row['Cantidad_de_palabras'] >= 46 and row['Cantidad_de_palabras'] <= 75) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Básico'	
    ## GRADO 4 PRIMARIA - NIVEL AVANZADO 
    if (row['Cantidad_de_palabras'] >= 76 and row['Cantidad_de_palabras'] <= 110) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Medio'		
    ## GRADO 3 PRIMARIA - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] > 110 ) and (row['CURSO_NORMALIZADO'] == '4°' and row['Nivel'] == 'Primario')  : return  'Avanzado'	
    ## ################################-
        
    ## GRADO 5 PRIMARIA - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 60) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Crítico'
    ## GRADO 5 PRIMARIA - NIVEL BÁSICO
    if (row['Cantidad_de_palabras'] >= 61 and row['Cantidad_de_palabras'] <= 90) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Básico'	
    ## GRADO 5 PRIMARIA - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 91 and row['Cantidad_de_palabras'] <= 125) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Medio'
    ## GRADO 5 PRIMARIA - NIVEL AVANZADO
    if (row['Cantidad_de_palabras'] > 125 ) and (row['CURSO_NORMALIZADO'] == '5°' and row['Nivel'] == 'Primario')  : return  'Avanzado'	
    ## ################################-
    
    ## GRADO 6 PRIMARIA - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 75) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Crítico'
    ## GRADO 6 PRIMARIA - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 76 and row['Cantidad_de_palabras'] <= 105) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Básico'	
    ## GRADO 6 PRIMARIA - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 106 and row['Cantidad_de_palabras'] <= 140) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Medio'
    ## GRADO 6 PRIMARIA - NIVEL AVANZADO
    if (row['Cantidad_de_palabras'] > 140 ) and (row['CURSO_NORMALIZADO'] == '6°' and row['Nivel'] == 'Primario')  : return  'Avanzado'	
    ## ################################-
        
    ## GRADO 7 PRIMARIA - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 85) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Crítico'
    ## GRADO 7 PRIMARIA - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 86 and row['Cantidad_de_palabras'] <= 115) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Básico'	
    ## GRADO 7 PRIMARIA - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 116 and row['Cantidad_de_palabras'] <= 155) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Medio'
    ## GRADO 7 PRIMARIA - NIVEL AVANZADO	
    if (row['Cantidad_de_palabras'] > 155 ) and (row['CURSO_NORMALIZADO'] == '7°' and row['Nivel'] == 'Primario')  : return  'Avanzado'
    ## ################################-
        
    ## CURSO 1 SECUNDARIAS - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 95) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
    ## CURSO 1 SECUNDARIAS - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 96 and row['Cantidad_de_palabras'] <= 125) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
    ## CURSO 1 SECUNDARIAS - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 126 and row['Cantidad_de_palabras'] <= 165) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
    ## CURSO 1 SECUNDARIAS - NIVEL AVANZADO	
    if (row['Cantidad_de_palabras'] > 165 ) and ((row['CURSO_NORMALIZADO'] == '1°' or row['CURSO_NORMALIZADO'] == '1º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
    ## ################################-
        
    ## CURSO 2 SECUNDARIAS - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 105) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
    ## CURSO 2 SECUNDARIAS - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 106 and row['Cantidad_de_palabras'] <= 135) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
    ## CURSO 2 SECUNDARIAS - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 136 and row['Cantidad_de_palabras'] <= 170) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
    ## CURSO 2 SECUNDARIAS - NIVEL AVANZADO	
    if (row['Cantidad_de_palabras'] > 170 ) and ((row['CURSO_NORMALIZADO'] == '2°' or row['CURSO_NORMALIZADO'] == '2º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
    ## ################################-
        
    ## CURSO 3 SECUNDARIAS - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 115) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
    ## CURSO 3 SECUNDARIAS - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 116 and row['Cantidad_de_palabras'] <= 145) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
    ## CURSO 3 SECUNDARIAS - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 146 and row['Cantidad_de_palabras'] <= 175) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
    ## CURSO 3 SECUNDARIAS - NIVEL AVANZADO	
    if (row['Cantidad_de_palabras'] > 175 ) and ((row['CURSO_NORMALIZADO'] == '3°' or row['CURSO_NORMALIZADO'] == '3º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
    ## ################################-
        
    ## CURSO 4 SECUNDARIAS - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 120) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
    ## CURSO 4 SECUNDARIAS - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 121 and row['Cantidad_de_palabras'] <= 150) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
    ## CURSO 4 SECUNDARIAS - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 151 and row['Cantidad_de_palabras'] <= 180) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
    ## CURSO 4 SECUNDARIAS - NIVEL AVANZADO	
    if (row['Cantidad_de_palabras'] > 180 ) and ((row['CURSO_NORMALIZADO'] == '4°' or row['CURSO_NORMALIZADO'] == '4º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
    ## ################################-
        
    ## CURSO 5 SECUNDARIAS - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 125) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
    ## CURSO 5 SECUNDARIAS - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 126 and row['Cantidad_de_palabras'] <= 155) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
    ## CURSO 5 SECUNDARIAS - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 156 and row['Cantidad_de_palabras'] <= 185) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
    ## CURSO 5 SECUNDARIAS - NIVEL AVANZADO	
    if (row['Cantidad_de_palabras'] > 185 ) and ((row['CURSO_NORMALIZADO'] == '5°' or row['CURSO_NORMALIZADO'] == '5º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
    ## ################################-
        
    ## CURSO 6 SECUNDARIAS - NIVEL CRÍTICO
    if (row['Cantidad_de_palabras'] >= 0 and row['Cantidad_de_palabras'] <= 125) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Crítico'
    ## CURSO 6 SECUNDARIAS - NIVEL BÁSICO	
    if (row['Cantidad_de_palabras'] >= 126 and row['Cantidad_de_palabras'] <= 155) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Básico'	
    ## CURSO 6 SECUNDARIAS - NIVEL MEDIO 
    if (row['Cantidad_de_palabras'] >= 156 and row['Cantidad_de_palabras'] <= 185) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Medio'
    ## CURSO 6 SECUNDARIAS - NIVEL AVANZADO	
    if (row['Cantidad_de_palabras'] > 185 ) and ((row['CURSO_NORMALIZADO'] == '6°' or row['CURSO_NORMALIZADO'] == '6º Bilingüe') and (row['Nivel'] == 'Secundario Orientado' or row['Nivel'] == 'Secundario Técnico'))  : return  'Avanzado'
    ## ################################-
    
def calcular_desempeño(listaDeColumnas, dF_dataFrameIzquierdo, dF_dataFrameDerecha, ColumnaY, ColumnaX, col_titulo):    
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