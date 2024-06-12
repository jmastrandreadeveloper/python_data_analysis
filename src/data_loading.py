import os
import pandas as pd
import chardet
import csv

class DataLoader:
    def __init__(self, filename):
        # Construye la ruta completa al archivo CSV
        self.filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', filename)

    def detect_csv_properties(self, filepath):
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

    def fetchCSV(self, archivoCSV):
        properties = self.detect_csv_properties(archivoCSV)
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

    def load_csv(self):
        # Verifica que el archivo exista
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"No se encontró el archivo: {self.filepath}")
        return self.fetchCSV(self.filepath)

    def load_excel(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"No se encontró el archivo: {self.filepath}")
        return pd.read_excel(self.filepath)
