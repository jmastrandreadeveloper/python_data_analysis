import pandas as pd
import sys
import os
# Añadir la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_loading import DataLoader

# Creación de un DataFrame desde un archivo CSV
# Los archivos CSV son una fuente común de datos. Puedes crear un DataFrame leyendo un archivo CSV.
print('_'*50 + '\nLeer un archivo CSV para crear un DataFrame\n' + '_'*50)
# Carga de datos
loader = DataLoader('data_000.csv')
df = loader.load_csv()
# Mostrar el DataFrame
print(df)
print('_'*50 + '\n' + '_'*50)