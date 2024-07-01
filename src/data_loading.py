import os
import pandas as pd
import src.utils as u

class DataLoader:
    def __init__(self, filename):
        # Construye la ruta completa al archivo CSV
        self.filepath = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', filename)
    
    def load_csv(self):
        # Verifica que el archivo exista
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"No se encontró el archivo: {self.filepath}")        
        return u.quitar_retorno_de_columnas(pd.read_csv(self.filepath , header=0 , delimiter=";" , encoding = "UTF-8" , lineterminator = '\n'))

    def load_excel(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"No se encontró el archivo: {self.filepath}")
        return pd.read_excel(self.filepath)
