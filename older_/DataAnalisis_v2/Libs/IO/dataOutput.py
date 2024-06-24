import pandas       as pd
import csv
import json
import numpy

df = pd.DataFrame()

def dataFrameToCSV(
        nombreArchivo,
        dF,
        dict = {
            'sep' : ';' ,
            'encoding' : 'UTF-8' , 
            'lineterminator' : '\n'
        }):
    try:
        # Quitar '\r' de los nombres de las columnas
        dF.columns = [c.replace('\r', 'a') for c in dF.columns]
        dF.to_csv(
            f'{nombreArchivo}.csv',
            sep = dict.get('sep') , encoding = dict.get('encoding') , lineterminator=dict.get('lineterminator'),
            #sep=';',
            #encoding='UTF-8-sig',
            #line_terminator='CRLF',
            quoting=csv.QUOTE_ALL,
            index=False,
            header=True
        )
    except:
        print('..check nombre de archivo o espacio en disco..!' , f'{nombreArchivo}.csv')
    else:
        
        print('..archivo ', nombreArchivo ,' grabado..!')
    return

def dataFrameToEXCEL(nombreArchivo , dF):
    return

def dataFrameToDict(dF, listaDeColumnas , props):
    """
    Convierte un DataFrame en una lista de diccionarios.
    La primera columna de 'listaDeColumnas' se usa como clave.
    """
    try:
        # Filtrar el DataFrame para quedarse solo con las columnas deseadas
        filtered_df = dF[listaDeColumnas]
        # Crear el diccionario principal
        dict_values = filtered_df.set_index(listaDeColumnas[0]).T.to_dict()
        # Crear una lista de diccionarios similar a un formato JSON
        list_dict_final = [{listaDeColumnas[0]: key, props: value} for key, value in dict_values.items()]
        # Obtener las claves del diccionario en una lista
        list_keys = list(dict_values.keys())
        list_keys.sort()
        return list_dict_final, dict_values , list_keys
    except Exception as e:
        print('Error al procesar el DataFrame:', e)
        return [], {}