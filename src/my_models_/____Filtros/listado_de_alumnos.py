import pandas as pd

def listado_de_alumnos(unaEscuela, dFrame , dict):    
    # Filtrar el DataFrame por 'Escuela_ID'
    rslt_df = dFrame[
            (dFrame['Escuela_ID'] == unaEscuela)
    ]
    
    # Eliminar la columna 'separador', si se desea eliminar una columna, se utiliza drop en lugar de pop.
    #rslt_df = rslt_df.drop(columns=['separador'])
    rslt_df = lib.UTILS.utils.eliminar_columna(rslt_df , dict.get('cols_delete') )
    
    # Reordenar las columnas según se especifica
    rslt_df = rslt_df.reindex(columns=dict.get('cols'))
    
    # Convertir el DataFrame a una lista de diccionarios con el formato deseado
    dict_listado_de_alumnos = rslt_df.to_dict(orient=dict.get('orient'))
    
    return dict_listado_de_alumnos