import pandas as pd
import sys
import os
# Añadir la raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.data_loading import DataLoader

print('\n')
# Creación de un DataFrame desde un archivo CSV
# Los archivos CSV son una fuente común de datos. Puedes crear un DataFrame leyendo un archivo CSV.
print('Leer un archivo CSV para crear un DataFrame')
# Carga de datos
loader = DataLoader('data_000.csv')
df = loader.load_csv()
# Mostrar el DataFrame
print(df,'\n')