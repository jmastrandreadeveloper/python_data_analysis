import os
from PIL import Image
import csv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

print('BASE_DIR ' , BASE_DIR)

def save_dataframe_to_csv(dataframe, filepath):
    try:
        dict = {
            'sep' : ';' ,
            'encoding' : 'UTF-8' , 
            'lineterminator' : '\n'
        }
        # Quitar '\r' de los nombres de las columnas
        dataframe.columns = [c.replace('\r', 'a') for c in dataframe.columns]
        dataframe.to_csv(
            f'{filepath}',
            sep = dict.get('sep') , encoding = dict.get('encoding') , lineterminator=dict.get('lineterminator'),            
            #quoting=csv.QUOTE_ALL,
            index=False,
            header=True
        )        
    except:
        print('..check nombre de archivo o espacio en disco..!' , f'{filepath}.csv')
    else:
        
        print('..archivo ', filepath ,' grabado..!')
    return
    

def ensure_dir(directory):
    # Obtiene la ruta absoluta del directorio a crear
    abs_directory = os.path.abspath(directory)
    print(f"Intentando asegurar el directorio: {abs_directory}")

    # Normaliza ambas rutas a minúsculas para evitar problemas de comparación
    normalized_abs_directory = abs_directory.lower()
    normalized_base_dir = BASE_DIR.lower()

    # Verifica que el directorio esté dentro de BASE_DIR
    if not normalized_abs_directory.startswith(normalized_base_dir):
        raise ValueError(f"El directorio {abs_directory} no está dentro de la carpeta base permitida {BASE_DIR}.")

    # Si no existe, crea el directorio
    if not os.path.exists(abs_directory):
        os.makedirs(abs_directory)
        print(f"Directorio creado: {abs_directory}")
    else:
        print(f"El directorio ya existe: {abs_directory}")

def save_image(image, filepath):
    # Asegura que el directorio del archivo exista
    ensure_dir(os.path.dirname(filepath))
    # Guarda la imagen
    image.save(filepath)
