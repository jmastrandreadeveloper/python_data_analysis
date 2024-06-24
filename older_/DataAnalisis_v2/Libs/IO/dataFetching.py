import pandas       as pd
import chardet
import csv
import requests
import json


def fetchCSV(archivoCSV):
    properties = detect_csv_properties(archivoCSV)
    print(properties)
    print('...fetching CSV file ...')

    # Lista de codificaciones alternativas para probar si la detección inicial falla
    codificaciones_alternativas = ['utf-8', 'latin1', 'ISO-8859-1']
    if properties['encoding'] in codificaciones_alternativas:
        codificaciones_alternativas.remove(properties['encoding'])

    dF = pd.DataFrame()
    try:
        # Intentar leer sin especificar lineterminator
        dF = pd.read_csv(archivoCSV, sep=properties.get('delimiter'), encoding=properties.get('encoding'))
    except Exception as e:
        print('Error al leer el archivo con la codificación detectada:', str(e))
        # Si falla, intentar con las codificaciones alternativas
        for encoding in codificaciones_alternativas:
            try:
                print(f"Intentando leer el archivo con codificación {encoding}...")
                dF = pd.read_csv(archivoCSV, sep=properties.get('delimiter'), encoding=encoding)
                print(f"Archivo leído exitosamente con codificación {encoding}.")
                break
            except Exception as e:
                print(f"Falló la lectura con codificación {encoding}: {str(e)}")
    else:
        if dF.empty:
            print("..error al leer el archivo:", archivoCSV)
        else:
            print('..archivo', archivoCSV, 'leído..!')
    return dF

# def fetchCSV(archivoCSV , dict):
#     properties = detect_csv_properties(archivoCSV)
#     print(properties)
#     # fetching .. leer los datos usando 
#     # -> prefix the string with r (to produce a raw string): o duplicate all backslashes \\
#     print('...fetching CSV file ...')
#     # sep_ = ';' , encoding_ = 'UTF-8' , lineterminator_ = 'CRLF'
#     dF = pd.DataFrame()
#     try:        
#         dF = pd.read_csv(archivoCSV ,  sep = dict.get('sep') , encoding = dict.get('encoding') , lineterminator=dict.get('lineterminator')) # pd.read_csv(archivoCSV ,  sep='\s*,\s*', engine='python', lineterminator='\n')
#         #dF = pd.read_csv(archivoCSV ,  sep = properties.get('delimiter') , encoding = properties.get('encoding') , lineterminator=properties.get('lineterminator')) # pd.read_csv(archivoCSV ,  sep='\s*,\s*', engine='python', lineterminator='\n')
#         ultima_columna = dF.columns[-1]
#         # quito el \r de la última columna para evitar problemas
#         dF.loc[:, ultima_columna] = dF[ultima_columna].str.replace('\r', '', regex=False)
#         dF.columns = [c.replace('\r', '') for c in dF.columns]
#         #print(dF[ultima_columna])
#     except:
#         print('..error al leer el archivo : ' , archivoCSV)
#     else:
#         print('..archivo ', archivoCSV ,' leído..!')
#     return dF

def fetchEXCEL(archivoXLSX):
    print('...leer EXCEL...')
    dF = pd.DataFrame()
    dF = pd.read_excel(archivoXLSX)
    return dF

def fetchSQL(sqlScript , dict):
    dF = pd.DataFrame()
    return dF

def fetchJSON(url):
    """
    # Ejemplo de uso
    if __name__ == "__main__":
        url = 'https://ejemplo.com/data.json'  # Sustituye por la URL de tu archivo JSON
        json_data = fetch_json(url)
        
        if json_data is not None:
            print(json_data)
        else:
            print("No fue posible obtener los datos.")
    """
    # Realiza una solicitud GET a la URL proporcionada
    response = requests.get(url)
    
    # Verifica que la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsea (convierte) el texto de la respuesta a JSON
        data = response.json()
        return data
    else:
        print(f"Error al realizar la solicitud: código de estado {response.status_code}")
        return None
    

def leer_json(ruta_archivo):
    """Carga el contenido de un archivo JSON en un objeto de Python.

    Args:
        ruta_archivo (str): La ruta al archivo JSON que se desea cargar.

    Returns:
        dict: El contenido del archivo JSON como un diccionario de Python.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON en el archivo {ruta_archivo}.")
    except Exception as e:
        print(f"Un error ocurrió al cargar el archivo {ruta_archivo}: {e}")


def detect_csv_properties(filepath):
    with open(filepath, 'rb') as file:
        rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

    # Si se detecta UTF-8-SIG, tratarlo simplemente como UTF-8
    if encoding == 'UTF-8-SIG':
        encoding = 'UTF-8'
    
    sample = None
    delimiter = None
    lineterminator = None
    
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            sample = file.read(4096)
    except UnicodeDecodeError:
        encoding = 'utf-8'  # Intento de recuperación con UTF-8 estándar
        with open(filepath, 'r', encoding=encoding) as file:
            sample = file.read(4096)
    
    if sample:
        try:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(sample)
            delimiter = dialect.delimiter
            lineterminator = dialect.lineterminator
        except csv.Error:
            delimiter = ','
            lineterminator = '\r\n'
    
    return {
        'encoding': encoding,
        'delimiter': delimiter,
        'lineterminator': lineterminator,
    }




################### fetching de datos en google drive :
"""
1. Acceso directo mediante link compartido
Si el archivo en Google Drive se ha compartido públicamente (o se te ha proporcionado el enlace directo de descarga), 
puedes descargarlo directamente usando la biblioteca requests. Esto funciona bien para archivos como CSV, JSON, etc.

Para obtener una URL de descarga directa de un archivo compartido en Google Drive, 
reemplaza la parte open?id= de la URL compartida por uc?export=download&id=.

import requests

def download_file_from_google_drive(url, destination):
    response = requests.get(url)
    with open(destination, "wb") as file:
        file.write(response.content)

# URL de descarga directa del archivo en Google Drive
url = 'URL_DIRECTA_DE_DESCARGA'

# Destino donde guardar el archivo
destination = 'path/to/your/file.csv'

download_file_from_google_drive(url, destination)

2. Uso de PyDrive o Google Drive API
Para un control más avanzado, puedes utilizar PyDrive o la API de Google Drive para acceder a archivos. 
Esto es útil si necesitas acceder a archivos no públicos o realizar operaciones más complejas. 
Aquí te muestro cómo hacerlo con PyDrive, que es un wrapper más sencillo de la API de Google Drive.

Primero, necesitarás instalar PyDrive: 
pip install PyDrive

Luego, deberás configurar la autenticación OAuth:

Ve a Google Developers Console.
Crea un proyecto.
Ve a "APIs & Services > Dashboard" y habilita "Drive API".
Ve a "Credentials", crea credenciales de tipo "OAuth client ID". Si te pide configurar la pantalla de consentimiento, hazlo.
Descarga el archivo JSON con las credenciales y guárdalo en tu proyecto.
Aquí tienes un ejemplo básico de cómo usar PyDrive para descargar un archivo:
"""

"""
Recuerda reemplazar 'TU_FILE_ID' por el ID real de tu archivo, el cual puedes obtener de la URL del archivo en Google Drive, y 
'nombre_de_tu_archivo.ext' por el nombre y extensión con los que deseas guardar el archivo localmente.

Cada uno de estos métodos tiene sus propias ventajas y puede ser más adecuado para diferentes casos de uso. 
El primer método es más sencillo para archivos públicos o compartidos con un enlace directo, 
mientras que el segundo ofrece más flexibilidad y control, especialmente para trabajar 
con archivos privados o realizar operaciones más complejas en Google Drive.


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Autenticación y creación del cliente PyDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Crea un servidor local y maneja la autenticación.
drive = GoogleDrive(gauth)

# ID del archivo a descargar (puedes obtenerlo de la URL de Google Drive)
file_id = 'TU_FILE_ID'

file = drive.CreateFile({'id': file_id})
file.GetContentFile('nombre_de_tu_archivo.ext')  # Extensión según el tipo de archivo
"""

################################################### guardar datos en google drive ###############################################

"""
Paso 1: Configurar Google Drive API
Ve a Google Developers Console.
Crea un nuevo proyecto o selecciona uno existente.
Busca y habilita Google Drive API para tu proyecto.
Ve a "Credenciales", haz clic en "Crear credenciales" y elige "ID de cliente de OAuth" (si no has configurado la pantalla de consentimiento, se te pedirá que lo hagas).
Descarga el archivo JSON con tus credenciales.
Paso 2: Instalar las bibliotecas necesarias
Instala google-api-python-client y google-auth usando pip:

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Paso 3: Autenticación y Subida de Archivos
Aquí tienes un ejemplo de script en Python para autenticar y subir un archivo a Google Drive:

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# Definir el alcance de la aplicación
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    creds = None
    # El archivo token.pickle almacena los tokens de acceso y actualización del usuario, y se
    # crea automáticamente cuando el flujo de autorización se completa por primera vez.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Si no hay credenciales válidas disponibles, pide al usuario que se autentique.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)  # Asegúrate de que 'credentials.json' es tu archivo de credenciales descargado
            creds = flow.run_local_server(port=0)
        # Guarda las credenciales para la próxima ejecución
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Subir un archivo a Google Drive
    file_metadata = {'name': 'nombre_archivo.ext'}  # Cambia 'nombre_archivo.ext' por el nombre de tu archivo
    media = MediaFileUpload('files/nombre_archivo.ext', mimetype='tipo_mime/ext')  # Cambia 'tipo_mime/ext' por el MIME type de tu archivo
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    print('Archivo subido con ID: %s' % file.get('id'))

if __name__ == '__main__':
    main()

Este script te guiará a través del proceso de autenticación la primera vez que lo ejecutes, 
abriendo una ventana en tu navegador para que inicies sesión en tu cuenta de Google y autorices a tu aplicación a acceder a Google Drive. 
Una vez autorizado, un token se almacenará en token.pickle, permitiendo accesos futuros sin necesidad de reautorización.
Recuerda reemplazar 'nombre_archivo.ext', 'files/nombre_archivo.ext', y 'tipo_mime/ext' con el nombre de tu archivo, 
la ruta al archivo que deseas subir, y el tipo MIME correcto de tu archivo, respectivamente.
Este ejemplo se enfoca en subir archivos a Google Drive con un alcance que permite a la aplicación acceder solo a archivos que ella misma ha creado. 
Si necesitas un acceso más amplio, puedes cambiar el alcance especificado en SCOPES.

"""

