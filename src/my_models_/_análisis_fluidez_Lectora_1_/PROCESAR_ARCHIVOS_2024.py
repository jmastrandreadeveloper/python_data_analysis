# en este módulo se van a consolidar las funciones para normalizar los archivos de FL
# desde su lectura y diferentes procesos que se vayan haciendo..
# la idea es porder reunir los procesos para un solo archivo y algunas funciones harán# procesos para mas de un archivo
import sys
sys.path.insert(1, 'F:\ProyectosPython\ProyectoBase\configuración')
sys.path.insert(1, 'D:\PROYECTOS PYTHON\ProyectoBase_v2\configuración')

import config as cf
import pandas as pd
import funcionesUtiles as fU
import numpy as np


sep_            = ';'
encoding_       = "UTF-8"
lineterminator_ = '\n'


def proceso_1_leer_archivos(
    PATH_BASES_DE_ENTRADA,
    NOMBRE_BASE_ENTRADA_FL,):
    """
    leer archivos
    """
     # leer el archivo .CSV
    dF = fU.seleccionarDataSet(
        PATH_BASES_DE_ENTRADA,
        NOMBRE_BASE_ENTRADA_FL,
        sep_,
        encoding_,
        lineterminator_
    )
    return dF

def proceso_2_normalizar_df_fl(    
    tipoDeDataFrame,
    dataFrame,
    normalizarNiveles,
    eliminarFilasEspecificas = True):
    """
    normalizarDataFrame tipoDeDataFrame , dataFrame , normalizarNiveles , eliminarFilasEspecificas = True
    """
    df_ = fU.normalizarDataFrame(
        tipoDeDataFrame,
        dataFrame,
        normalizarNiveles,
        eliminarFilasEspecificas = True
    )
    return df_

def proceso_3_alumnos_incluidos_SI(
    df_,
    PATH_BASES_DE_SALIDA,
    NOMBRE_BASE_SALIDA_FL,):
    """
    No borrarlas
    extaer filas alumnos incluidos = SI
    """
    df_alumnos_incluidos_SI = df_[df_['Incluido'] == 'Si']

    archivoFinal_alumnos_incluidos_SI = f"{PATH_BASES_DE_SALIDA}{'/proceso_3_' + NOMBRE_BASE_SALIDA_FL[:-17]}_con_alumnos_incluidos_SI.csv"
    df_alumnos_incluidos_SI.to_csv(archivoFinal_alumnos_incluidos_SI, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    return df_alumnos_incluidos_SI

def proceso_4_alumnos_incluidos_NO(
    df_,
    PATH_BASES_DE_SALIDA,
    NOMBRE_BASE_SALIDA_FL,):
    """
    No borrarlas
    extaer filas alumnos incluidos = NO
    """    
    df_alumnos_incluidos_NO = df_[df_['Incluido'] == 'No']

    archivoFinal_alumnos_incluidos_NO = f"{PATH_BASES_DE_SALIDA}{'/proceso_4_' + NOMBRE_BASE_SALIDA_FL[:-17]}_con_alumnos_incluidos_NO.csv"
    df_alumnos_incluidos_NO.to_csv(archivoFinal_alumnos_incluidos_NO, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    return df_alumnos_incluidos_NO

def proceso_5_alumnos_con_DESEMPEÑO_y_sin_DESEMPEÑO(
    df_,
    PATH_BASES_DE_SALIDA,
    NOMBRE_BASE_SALIDA_FL,):
    """
    No borrarlas
    extaer filas CON DESEMPEÑO Y SIN DESEMPEÑO
    """
    df_con_DESEMPEÑO = df_[df_['DESEMPEÑO'] != '-']
    archivoFinal_con_DESEMPEÑO = f"{PATH_BASES_DE_SALIDA}{'/proceso_5_' + NOMBRE_BASE_SALIDA_FL[:-17]}_con_DESEMPEÑO.csv"
    df_con_DESEMPEÑO.to_csv(archivoFinal_con_DESEMPEÑO, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    df_sin_DESEMPEÑO = df_[df_['DESEMPEÑO'] == '-']
    archivoFinal_sin_DESEMPEÑO = f"{PATH_BASES_DE_SALIDA}{'/proceso_5_' + NOMBRE_BASE_SALIDA_FL[:-17]}_sin_DESEMPEÑO.csv"
    df_sin_DESEMPEÑO.to_csv(archivoFinal_sin_DESEMPEÑO, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    return df_con_DESEMPEÑO , df_sin_DESEMPEÑO

def proceso_6_extraer_filas_cant_palabras_menores_y_mayores_a_300(df, PATH_BASES_DE_SALIDA, NOMBRE_BASE_SALIDA_FL):
    """
    No borrarlas
    extraer_filas_cant_palabras_mayores_a_300
    va a devolver dos dataframes el que tiene menos de 300 y el que tiene mas de 300
    """
    # Hacer una copia del DataFrame original para evitar SettingWithCopyWarning
    df = df.copy()

    # Convertir los valores de 'Cantidad_de_palabras' a números, reemplazando los no numéricos con NaN
    df['Cantidad_de_palabras'] = pd.to_numeric(df['Cantidad_de_palabras'], errors='coerce')

    # Crear DataFrames separados para valores menores y mayores o iguales a 300
    df_menor_a_300 = df[df['Cantidad_de_palabras'] < 300].copy()
    df_mayor_a_300 = df[df['Cantidad_de_palabras'] >= 300].copy()

    # Guardar los DataFrames resultantes en archivos CSV
    archivoFinal_menor_a_300 = f"{PATH_BASES_DE_SALIDA}/proceso_6_{NOMBRE_BASE_SALIDA_FL[:-4]}_sin_mayores_a_300.csv"
    df_menor_a_300.to_csv(archivoFinal_menor_a_300, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    archivoFinal_mayor_a_300 = f"{PATH_BASES_DE_SALIDA}/proceso_6_{NOMBRE_BASE_SALIDA_FL[:-4]}_con_mayores_a_300.csv"
    df_mayor_a_300.to_csv(archivoFinal_mayor_a_300, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    return df_menor_a_300, df_mayor_a_300

def proceso_7_buscar_MAX_cantidad_de_palabras(
    df_,
    PATH_BASES_DE_SALIDA,
    NOMBRE_BASE_SALIDA_FL,):
    """
    graba el archivo, se va a quedar con la mejor medición..
    buscar_MAX_cantidad_de_palabras

    def obtener_mejor_medicion_por_alumno(df, columna_id='Alumno_ID', columna_medicion='Cantidad_de_palabras'):

        # Convertir los valores de 'Cantidad_de_palabras' a números, reemplazando los no numéricos con NaN
        df[columna_medicion] = pd.to_numeric(df[columna_medicion], errors='coerce')

        # Ordenar por 'Cantidad_de_palabras' en orden descendente y eliminar duplicados por 'Alumno_ID'
        df_mejores_mediciones = df.sort_values(by=columna_medicion, ascending=False).drop_duplicates(subset=[columna_id])

    """
    def convert_to_int_or_str(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return '-'
    #############################################################################################################    
    df_new = df_.sort_values('Cantidad_de_palabras', ascending=False).drop_duplicates(['Alumno_ID']).sort_index()

    for col in ['Edad', 'Cantidad_de_palabras', 'Prosodia', 'subcue']:
        df_new[col] = pd.to_numeric(df_new[col], errors='coerce').fillna('-').apply(convert_to_int_or_str)

    df_filtered = df_new[df_new['Cantidad_de_palabras'].apply(lambda x: isinstance(x, int) and x < 300 or x == '-')]
    df_mejores_mediciones = df_filtered.sort_values(by='Cantidad_de_palabras', ascending=False).drop_duplicates(subset=['Alumno_ID'])

    archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_7_' + NOMBRE_BASE_SALIDA_FL}"
    df_mejores_mediciones.to_csv(archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    return df_filtered





def proceso_para_fluidez_operativo_1():
    """
    todos los procesos previos y 
    acá se van a hacer los agrupamientos para cuando toca hacer el primer operativo del año
    """
    return

def proceso_para_fluidez_operativo_2(
    diccionarioEscuelas ,
    datosFluidez_1,
    datosFluidez_2,
    nombreArchivoUnidos,
    nombreArchivoPrimerYSegundoOperativos,
    PATH_BASES_DE_SALIDA):
    """
    todos los procesos previos y
    acá se van a hacer los agrupamientos para cuando toca hacer el segundo operativo del año
    """

    diccionarioFludezLectoraNormalizado_primera_medición = {}
    diccionarioFludezLectoraNormalizado_segunda_medición = {}

    def tipoDesempeño2(x):
        """
        diccionarioDesempeño = {'Crítico'   : 0 ,
                                'Básico'    : 1 ,
                                'Medio'     : 2 ,
                                'Avanzado'  : 3 ,
                                '0'         : 'Sin comparativa'
                                }
        """
        if x == 'Crítico':
            return 0
        elif x == 'Básico':
            return 1
        elif x == 'Medio':
            return 2
        elif x == 'Avanzado':
            return 3
        else:
            return '-1'

    def cambiar_nombres_de_columnas_fl_1_fl_2():
        print('cambiar_nombres_de_columnas_fl_1_fl_2')
        # cambiar nombres de las columnas para fl 1
        datosFluidez_1.rename(
            columns = {
                'DESEMPEÑO'             : 'DESEMPEÑO_primer_op' , 
                'Cantidad_de_palabras'  : 'Cantidad_de_palabras_primer_op' , 
                'Prosodia'              : 'Prosodia_primer_op',
                'separador'             : 'separador_1' 
            }, 
            inplace = True
        )
        # cambiar nombres de las columnas para fl 2
        datosFluidez_2.rename(
            columns = {
                'DESEMPEÑO'             : 'DESEMPEÑO_segundo_op' , 
                'Cantidad_de_palabras'  : 'Cantidad_de_palabras_segundo_op' , 
                'Prosodia'              : 'Prosodia_segundo_op',
                'separador'             : 'separador_2' 
            }, 
            inplace = True
        )
        return 
    
    def fusionar_data_frames_nominal_fl_1_y_f_l2_2():
        print('fusionar_data_frames_nominal_fl_1_y_f_l2_2')
        listaDeDataFrames = [
            diccionarioEscuelas.get('dataframe_normalizado'),
            datosFluidez_1,
            datosFluidez_2
        ]
        dF_mergueados  = fU.fusionarDataFrames(listaDeDataFrames , 'Alumno_ID')
        # renombrar la columna 'DESEMPEÑO'
        dF_mergueados.rename(columns={
            'DESEMPEÑO'            :   'DESEMPEÑO_primer_op' 
        }, inplace = True)
        return dF_mergueados
    
    def recortar_columnas(dataFrame , listaDeColumnas):
        print('...recortando dataframe...')
        # Verificar y eliminar índices duplicados
        if dataFrame.index.duplicated().any():
            print('..índices duplicados detectados..!')
            duplicated_indices = dataFrame.index[dataFrame.index.duplicated()]
            print(duplicated_indices)            
            # Eliminar índices duplicados manteniendo la primera aparición
            dataFrame = dataFrame[~dataFrame.index.duplicated(keep='first')]            
            # Resetear el índice para asegurarnos de que es único
            dataFrame = dataFrame.reset_index(drop=True)
        
        # Verificar nuevamente si el índice es único después del reseteo
        if dataFrame.index.duplicated().any():
            raise ValueError("El índice aún contiene duplicados después de resetear. Verifica los datos.")
        
        # Filtrar las columnas deseadas   
        dataFrameRecortado = dataFrame.loc[:, listaDeColumnas]
        try:
            #... borrar todas las filas donde el CURSO_NORMALIZADO sea igual a cero 0...
            dataFrameRecortado = dataFrameRecortado[dataFrameRecortado['CURSO_NORMALIZADO'] != 0]        
        except:
            pass
        print('...fin recortar dataframe...')        
        return dataFrameRecortado
    
    def normalizarMergueado(dataFrame):
        print('...normalizando mergueado...')
        try:
            dataFrame.loc[dataFrame['DESEMPEÑO_primer_op']  == 0 , 'DESEMPEÑO_primer_op']  = 'Sin determinar'
            dataFrame.loc[dataFrame['DESEMPEÑO_segundo_op'] == 0 , 'DESEMPEÑO_segundo_op'] = 'Sin determinar'
            dataFrame['DNI'] = dataFrame['DNI'].astype(int)
            dataFrame['Cantidad_de_palabras_primer_op'] = dataFrame['Cantidad_de_palabras_primer_op'].astype(int)
            dataFrame['Cantidad_de_palabras_segundo_op'] = dataFrame['Cantidad_de_palabras_segundo_op'].astype(int)
            dataFrame['DESEMPEÑO_primer_op'] = dataFrame['DESEMPEÑO_primer_op'].astype(str)
            dataFrame['DESEMPEÑO_segundo_op'] = dataFrame['DESEMPEÑO_segundo_op'].astype(str)    
            dataFrame['Escuela_ID'] = dataFrame['Escuela_ID'].astype(int)
        except:
            pass

        try:
            dataFrame['DNI'] = dataFrame['DNI'].astype(int)
            dataFrame['Cant. palabras 1° medición'] = dataFrame['Cant. palabras 1° medición'].astype(int)
            dataFrame['Cant. palabras 2° medición'] = dataFrame['Cant. palabras 2° medición'].astype(int)
            dataFrame['DESEMPEÑO_primer_op'] = dataFrame['DESEMPEÑO_primer_op'].astype(str)
            dataFrame['Desempeño 2° medición'] = dataFrame['Desempeño 2° medición'].astype(str)    
            dataFrame['Escuela_ID'] = dataFrame['Escuela_ID'].astype(int)
        except:
            pass

        print('borrar la columna DESEMPEÑO_primer_op')
        dataFrame_ = dataFrame
        dataFrame = dataFrame_.iloc[:, [i for i in range(dataFrame_.shape[1]) if i != 15]]
        sep_            = ';'
        encoding_       = "UTF-8"
        lineterminator_ = '\n'
        archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_8_' + 'para comprobar_1.csv'}"
        dataFrame.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)
        
        return dataFrame
    
    def reemplazarDesempeñoPorCodigo_PARA_DOS_OPERATIVOS2(dataframe):        
        #   dataframe.replace({'DESEMPEÑO_primer_op': {r'\\r': ''}}, regex=True , inplace = True)
        dataframe['DESEMPEÑO_primer_op_'] = dataframe['DESEMPEÑO_primer_op'].apply(tipoDesempeño2)
        dataframe['DESEMPEÑO_segundo_op_'] = dataframe['DESEMPEÑO_segundo_op'].apply(tipoDesempeño2)
        dataframe['DESEMPEÑO_primer_op_'] = dataframe['DESEMPEÑO_primer_op_'].astype(int)
        dataframe['DESEMPEÑO_segundo_op_'] = dataframe['DESEMPEÑO_segundo_op_'].astype(int)

        sep_            = ';'
        encoding_       = "UTF-8"
        lineterminator_ = '\n'
        archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_9_' + 'para comprobar_2_reemplazarDesempeñoPorCodigo.csv'}"
        dataframe.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)
        
        return dataframe
    
    def comparativaDesempeño(dataframe):
        print('...haciendo comparativa de desempeños...')
        # https://www.statology.org/compare-two-columns-in-pandas/
        #dataframe.loc[dataframe['DESEMPEÑO_primer_op_'].eq('Sin desempeño'), 'Births'] = 'Unknown'
        #if dataframe['DESEMPEÑO_primer_op_'] == 'Sin desempeño':
        #    print('no compara')
        # https://www.geeksforgeeks.org/how-to-compare-two-columns-in-pandas/
        #dataframe['compara'] = np.where((dataframe['DESEMPEÑO_segundo_op_'] == dataframe['DESEMPEÑO_primer_op_']) , 'Se Mantiene' , 'sin comparación')
        #dataframe['compara'] = np.where((dataframe['DESEMPEÑO_segundo_op_'] > dataframe['DESEMPEÑO_primer_op_'])  , 'Mejoró' , 'sin comparación')
        #dataframe['compara'] = np.where((dataframe['DESEMPEÑO_segundo_op_'] < dataframe['DESEMPEÑO_primer_op_'])  , 'Bajó' , 'sin comparación')
        #define conditions
        conditions = [  dataframe['DESEMPEÑO_primer_op_'] > dataframe['DESEMPEÑO_segundo_op_'], 
                        dataframe['DESEMPEÑO_primer_op_'] < dataframe['DESEMPEÑO_segundo_op_'],
                        dataframe['DESEMPEÑO_primer_op_'] == dataframe['DESEMPEÑO_segundo_op_']
                    ]

        #define choices
        choices = ['Bajó de nivel', 'Subió de nivel' , 'Se Mantuvo']

        #create new column in DataFrame that displays results of comparisons
        dataframe['compara'] = np.select(conditions, choices, default='Sin comparación')
        dataframe.loc[dataframe['DESEMPEÑO_primer_op'] == 'Sin determinar', 'compara'] = 'Sin determinar'
        dataframe.loc[dataframe['DESEMPEÑO_segundo_op'] == 'Sin determinar', 'compara'] = 'Sin determinar'
        #dataframe['compara'] = np.where((dataframe['DESEMPEÑO_primer_op'] == 'Sin determinar' or dataframe['DESEMPEÑO_segundo_op'] == 'Sin determinar')  , 'sin comparación' , 'sin comparación')

        # reordenar la nueva columna, ponerla antes de los dos separadores
        columnas_reordenadas = [
            'Alumno_ID',
            'DNI',
            'Apellido_Alumno',
            'Nombre_Alumno',
            'CURSO_NORMALIZADO',
            'División',
            'Nivel',
            'NivelOriginal',
            'Gestión',
            'Supervisión',
            'Escuela_ID',
            'Número_escuela',
            'Nombre_Escuela',
            'Departamento',
            'Localidad',
            'DESEMPEÑO_primer_op',
            'Cantidad_de_palabras_primer_op',
            'Prosodia_primer_op',
            'DESEMPEÑO_segundo_op',
            'Cantidad_de_palabras_segundo_op',
            'Prosodia_segundo_op',
            'DESEMPEÑO_primer_op_',
            'DESEMPEÑO_segundo_op_',
            'compara',
            'separador_1',
            'separador_2',
            
        ]

        # cambiar los tipos de valores para las siguientes columnas:
        # Escuela_ID
        # Cantidad_de_palabras_primer_op
        # Cantidad_de_palabras_segundo_op
        dataframe['Escuela_ID'] = dataframe['Escuela_ID'].astype(int)
        dataframe['Cantidad_de_palabras_primer_op'] = dataframe['Cantidad_de_palabras_primer_op'].astype(int)
        dataframe['Cantidad_de_palabras_segundo_op'] = dataframe['Cantidad_de_palabras_segundo_op'].astype(int)

        dataframe = dataframe[columnas_reordenadas]
        
        sep_            = ';'
        encoding_       = "UTF-8"
        lineterminator_ = '\n'

        archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_10_' + 'para comprobar_3_comparativaDesempeño.csv'}"
        dataframe.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

        #print(dataframe)

        return dataframe
    
    def eliminarFilas_Sin_determinar(dataframe):
        print('...eliminando filas sin determinar y que estan con curso en cero..')
        try:
            dataframe.drop(dataframe[dataframe['CURSO_NORMALIZADO'] == (0)].index, inplace = True)
        except:
            pass
        try:
            dataframe.drop(dataframe[dataframe['Curso'] == (0)].index, inplace = True)
        except:
            pass
        try:
            dataframe.drop(dataframe[dataframe['compara'] == ('Sin determinar')].index, inplace = True)
        except:
            pass
        try:
            dataframe.drop(dataframe[dataframe['Cantidad_de_palabras_primer_op'] > 299].index, inplace = True)    
        except:
            pass
        try:
            dataframe.drop(dataframe[dataframe['Cantidad_de_palabras_segundo_op'] > 299].index, inplace = True) 
        except:
            pass
        print('...fin eliminando filas sin determinar y que estan con curso en cero..')


        

        sep_            = ';'
        encoding_       = "UTF-8"
        lineterminator_ = '\n'

        archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_11_' + 'para comprobar_4_eliminarFilas_Sin_determinar.csv'}"
        dataframe.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

        return dataframe
    
    def cambiarNombresDeColumnas(dataFrame , diccionarioColumnasACambiar):
        print('...cambiando nombres de columnas...')
        dataFrame.rename(columns = diccionarioColumnasACambiar, inplace = True)
        print('...fin cambiando nombres de columnas...')
        return dataFrame   
        

    cambiar_nombres_de_columnas_fl_1_fl_2()
    dF_fusionados = fusionar_data_frames_nominal_fl_1_y_f_l2_2()
    # DEJAR LAS SIGUIENTES COLUMNAS ...
    listaDeColumnas_a=['Alumno_ID','DNI','Apellido_Alumno','Nombre_Alumno','CURSO_NORMALIZADO','División','Nivel','NivelOriginal','Gestión','Supervisión','Escuela_ID','Número_escuela','Nombre_Escuela','Departamento','Localidad','DESEMPEÑO_primer_op','Cantidad_de_palabras_primer_op','Prosodia_primer_op','DESEMPEÑO_segundo_op','Cantidad_de_palabras_segundo_op','Prosodia_segundo_op','separador_1','separador_2',]
    dF_recortado = recortar_columnas(dF_fusionados , listaDeColumnas_a)
    
    sep_            = ';'
    encoding_       = "UTF-8"
    lineterminator_ = '\n'


    archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_12_' + 'para comprobar_7_dF_recortado.csv'}"
    dF_recortado.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)
    
    dF_normalizado = normalizarMergueado(dF_recortado)
    dF_reemplazado = reemplazarDesempeñoPorCodigo_PARA_DOS_OPERATIVOS2(dF_normalizado)
    dF_comparado = comparativaDesempeño(dF_reemplazado)    

    df_aux = pd.DataFrame()
    df_aux = eliminarFilas_Sin_determinar(dF_comparado) 
    
    # eliminar filas repetidas de alumnos
    # eliminar filas repetidas de alumnos
    # eliminar filas repetidas de alumnos
    # eliminar filas repetidas de alumnos
    # eliminar filas de alumnos id repetidos
    
    dF_re_procesado = df_aux.drop_duplicates(subset=['Alumno_ID'])
    archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_10_' + 'para comprobar_3_comparativaDesempeño_dF_re_procesado.csv'}"
    dF_re_procesado.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)
    
    dF_fusionados_primera_y_segunda    = fU.fusionarDataFrames([datosFluidez_1,datosFluidez_2] , 'Alumno_ID')

    listaDeColumnasAConservar=['Alumno_ID','Nivel_y','NivelOriginal_y','Escuela_ID_y','DESEMPEÑO_primer_op','DESEMPEÑO_segundo_op','DNI_y','Apellido_Alumno_y','Nombre_Alumno_y','CURSO_NORMALIZADO_y','División_y','Cantidad_de_palabras_primer_op','Cantidad_de_palabras_segundo_op','separador_1','separador_2',]
    dF_fusionados_primera_y_segunda_    = recortar_columnas(dF_fusionados_primera_y_segunda , listaDeColumnasAConservar)
    

    archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_13_' + 'para comprobar_6_recorte.csv'}"
    dF_fusionados_primera_y_segunda_.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)

    #dF_fusionados_primera_y_segunda_.to_csv('D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\para comprobar_6_recorte.csv', sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)        

    dF_fusionados_primera_y_segunda__   = cambiarNombresDeColumnas(dF_fusionados_primera_y_segunda_ , {'Cantidad_de_palabras_primer_op' : 'Cant. palabras 1° medición' ,'Cantidad_de_palabras_segundo_op' : 'Cant. palabras 2° medición' , 'Nivel_y' : 'Nivel' , 'NivelOriginal_y': 'NivelOriginal' , 'Escuela_ID_y' : 'Escuela_ID', 'DNI_y' : 'DNI' , 'Apellido_Alumno_y' : 'Apellido' , 'Nombre_Alumno_y' : 'Nombre' , 'CURSO_NORMALIZADO_y' : 'Curso' , 'División_y' : 'Div.' , 'DESEMPEÑO_primer_op' :  'Desempeño 1° medición'  , 'DESEMPEÑO_segundo_op' : 'Desempeño 2° medición'})
    
    archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_14_' + 'para comprobar_7_cambiarNombresDeColumnas.csv'}"
    dF_fusionados_primera_y_segunda__.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)
    #dF_fusionados_primera_y_segunda__.to_csv('D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\para comprobar_7_cambiarNombresDeColumnas.csv', sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)        

    dF_fusionados_primera_y_segunda___  = eliminarFilas_Sin_determinar(dF_fusionados_primera_y_segunda__)
    
    archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_15_' + 'para comprobar_8_eliminarFilas_Sin_determinar.csv'}"
    dF_fusionados_primera_y_segunda___.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)
    #dF_fusionados_primera_y_segunda___.to_csv('D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\para comprobar_8_eliminarFilas_Sin_determinar.csv', sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)        
    
    
    dF_fusionados_primera_y_segunda____ = normalizarMergueado(dF_fusionados_primera_y_segunda___)    
    dF_fusionados_primera_y_segunda____.sort_values(by =    [   'Curso' , 
                                                                'Div.' , 
                                                                'Apellido'
                                                            ]         ,
                                                            ascending = True                        , 
                                                            inplace=True                            ,
                                                            kind='quicksort'                        , 
                                                            na_position='first'                     , 
                                                            ignore_index=True                       , 
                                                            key=None
                                                    )
    
    dF_fusionados_primera_y_segunda____['Escuela_ID'] = dF_fusionados_primera_y_segunda____['Escuela_ID'].astype(int)
    
    
    # agrego una columna al final
    dF_fusionados_primera_y_segunda____['fin'] = 'fin'

    archivoFinal_ = f"{PATH_BASES_DE_SALIDA}{'/proceso_16_' + 'para comprobar_9_.csv'}"
    dF_fusionados_primera_y_segunda____.to_csv( archivoFinal_, sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)
    #dF_fusionados_primera_y_segunda____.to_csv('D:\PROYECTOS PYTHON\ProyectoBase_v2\scripts\FL_Op_2_Agosto_2024\DatosDeSalida\para comprobar_9_.csv', sep=sep_, encoding=encoding_, line_terminator=lineterminator_, index=False, header=True)        

    listaDeColumnasParaEscuelasNormalizadas_ = ['Escuela_ID' , 'Número_escuela' , 'Nombre_Escuela' , 'Nivel' , 'NivelOriginal' , 'Supervisión' , 'Departamento' , 'Regional']
    print('...generando lista de objetos escuela de la primera medición...')
    
    diccionarioFludezLectoraNormalizado_primera_medición = {
        'dataframe_fluidez_lectora_normalizado' : datosFluidez_1
    }

    miListaDeEscuelasCompletasNormalizadas_op_1 = fU.crearListaDeDatos(diccionarioFludezLectoraNormalizado_primera_medición.get('dataframe_fluidez_lectora_normalizado') , listaDeColumnasParaEscuelasNormalizadas_ , False )
    ListadoDeObjetosEscuela_op_1 = fU.generarListaDeObjetosEscuela(diccionarioFludezLectoraNormalizado_primera_medición.get('dataframe_fluidez_lectora_normalizado') , miListaDeEscuelasCompletasNormalizadas_op_1)
    print('...generando lista de objetos escuela de la segunda medición...')
    
    diccionarioFludezLectoraNormalizado_segunda_medición = {
        'dataframe_fluidez_lectora_normalizado' : datosFluidez_2
    }

    miListaDeEscuelasCompletasNormalizadas_op_2 = fU.crearListaDeDatos(diccionarioFludezLectoraNormalizado_segunda_medición.get('dataframe_fluidez_lectora_normalizado') , listaDeColumnasParaEscuelasNormalizadas_ , False ) 
    ListadoDeObjetosEscuela_op_2 = fU.generarListaDeObjetosEscuela(diccionarioFludezLectoraNormalizado_segunda_medición.get('dataframe_fluidez_lectora_normalizado') , miListaDeEscuelasCompletasNormalizadas_op_2)    
    print('..fin proceso_para_fluidez_operativo_2')
    return [
        diccionarioFludezLectoraNormalizado_primera_medición    , 
        diccionarioFludezLectoraNormalizado_segunda_medición    , 
        
        dF_re_procesado                                         , # antes era dF_recortado 
        
        dF_fusionados_primera_y_segunda____                     ,
        ListadoDeObjetosEscuela_op_1                            ,
        ListadoDeObjetosEscuela_op_2
    ]

def crear_lista_dos_operativos(
        lista_de_objetos_escuelas,
        ListadoDeObjetosEscuela_op_1,
        ListadoDeObjetosEscuela_op_2):
    # esta función lo que hace es verificar cuales escuelas son las que tienen
    # los dos operativos y cuales las que no, entonces luego se recorrerá la lista
    # y de pendiendo de si tiene o no los dos informes, se hará el informe de comparativa
    lista_de_escuelas_con_dos_operativos = [] # esta lista tiene todas las escuelas --> lista_de_objetos_escuelas
    lista_de_escuelas_que_le_falta_el_primer_operativo = [] # esta lista tiene el primer operativo
    lista_de_escuelas_que_le_falta_el_segundo_operativo = [] # esta lista tiene el segundo operativo
    for escuela in lista_de_objetos_escuelas:
        en_op_1 = any(e.Escuela_ID == escuela.Escuela_ID for e in ListadoDeObjetosEscuela_op_1)
        en_op_2 = any(e.Escuela_ID == escuela.Escuela_ID for e in ListadoDeObjetosEscuela_op_2)
        
        if en_op_1 and en_op_2:
            lista_de_escuelas_con_dos_operativos.append(escuela)
        elif not en_op_1 and en_op_2:
            lista_de_escuelas_que_le_falta_el_primer_operativo.append(escuela)
        elif en_op_1 and not en_op_2:
            lista_de_escuelas_que_le_falta_el_segundo_operativo.append(escuela)
    
    return (
        lista_de_escuelas_con_dos_operativos, 
        lista_de_escuelas_que_le_falta_el_primer_operativo, 
        lista_de_escuelas_que_le_falta_el_segundo_operativo
    )

def proceso_para_fluidez_operativo_3():
    """
    todos los procesos previos y
    acá se van a hacer los agrupamientos para cuando toca hacer el tercer operativo del año
    """
    return