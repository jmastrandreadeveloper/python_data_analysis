# Limpieza de Datos con pandas
# En este tutorial, aprenderás cómo limpiar y preparar datos en pandas. 
# La limpieza de datos es un paso crucial en el análisis de datos, 
# ya que los datos en el mundo real a menudo están incompletos, 
# contienen errores o están en formatos inconsistentes.

import pandas as pd

print('_'*50 + '\n 0_Crear un DataFrame de ejemplo con valores nulos______________\n' + '_'*50)
data = {
    'Nombre': ['Ana', 'Luis', None, 'Marta'],
    'Edad': [28, None, 29, 42],
    'Ciudad': ['Guaymallén', 'Godoy Cruz', 'San Rafael', None]
}
df = pd.DataFrame(data)
print(df)

# 1-Manejo de Valores Nulos
# Identificar valores nulos
# Puedes identificar valores nulos en un DataFrame utilizando isnull y sum.

print('_'*50 + '\n_1-1_Identificar valores nulos_____________\n' + '_'*50)
print(df.isnull())

print('_'*50 + '\n_1-2_Contar valores nulos por columna_____________\n' + '_'*50)
print(df.isnull().sum())

# Puedes eliminar filas o columnas que contienen valores nulos utilizando dropna.
print('_'*50 + '\n_1-3_Eliminar filas con cualquier valor nulo_____________\n' + '_'*50)
# Eliminar filas con cualquier valor nulo
df_sin_nulos = df.dropna()
print(df_sin_nulos)

print('_'*50 + '\n_1-4_Eliminar columnas con cualquier valor nulo_____________\n' + '_'*50)
# Eliminar columnas con cualquier valor nulo
df_sin_nulos_col = df.dropna(axis=1)
print(df_sin_nulos_col)

# Rellenar valores nulos
# Puedes rellenar valores nulos con un valor específico o utilizando métodos como fillna.
# Rellenar valores nulos con un valor específico
print('_'*50 + '\n_1-5_Rellenar valores nulos con un valor específico_____________\n' + '_'*50)
df_rellenado = df.fillna({'Nombre': 'Desconocido', 'Edad': 0, 'Ciudad': 'Desconocida'})
print(df_rellenado)

# Rellenar valores nulos con el valor anterior en la columna
print('_'*50 + '\n_1-6_Rellenar valores nulos con el valor anterior en la columna_____________\n' + '_'*50)
df_rellenado_ffill = df.fillna(method='ffill')
print(df_rellenado_ffill)

# 2. Eliminación de Duplicados
print('_'*50 + '\n_2. Eliminación de Duplicados_____________\n' + '_'*50)
# Puedes eliminar filas duplicadas utilizando drop_duplicates.
# Crear un DataFrame de ejemplo con duplicados
data = {
    'Nombre': ['Ana', 'Luis', 'Ana', 'Marta'],
    'Edad': [28, 34, 28, 42],
    'Ciudad': ['Guaymallén', 'Godoy Cruz', 'Guaymallén', 'San Martín']
}
df = pd.DataFrame(data)
print(df)

# Eliminar filas duplicadas
print('_'*50 + '\n_2-1_Eliminar filas duplicadas_____________\n' + '_'*50)
df_sin_duplicados = df.drop_duplicates()
print(df_sin_duplicados)

# 3. Transformación de Datos
print('_'*50 + '\n_3. Transformación de Datos_____________\n' + '_'*50)
# Cambio de tipo de datos
# Puedes cambiar el tipo de datos de una columna utilizando astype.
# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': ['28', '34', '29', '42']
}
df = pd.DataFrame(data)
print(df)

# Cambiar el tipo de datos de la columna 'Edad' a entero
print('_'*50 + '\n_3-1_Cambiar el tipo de datos de la columna Edad a entero_\n' + '_'*50)
df['Edad'] = df['Edad'].astype(int)
print(df.dtypes)

# Renombrar columnas
# Puedes renombrar columnas utilizando rename.
# Renombrar columnas
print('_'*50 + '\n_3-2_Renombrar columnas_\n' + '_'*50)
df_renombrado = df.rename(columns={'Nombre': 'Nombre_Completo', 'Edad': 'Años'})
print(df_renombrado)

# 4. Trabajo con Fechas
print('_'*50 + '\n_4. Trabajo con Fechas_\n' + '_'*50)
# Convertir columnas a tipo datetime
# Puedes convertir columnas a tipo datetime utilizando pd.to_datetime.
# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Fecha': ['2023-01-01', '2023-05-12', '2023-07-19', '2023-11-30']
}
df = pd.DataFrame(data)
print(df)

# Convertir la columna 'Fecha' a tipo datetime
print('_'*50 + '\n_4-1_Convertir la columna Fecha a tipo datetime\n' + '_'*50)
df['Fecha'] = pd.to_datetime(df['Fecha'])
print(df.dtypes)

# Extraer el año, mes y día
df['Año'] = df['Fecha'].dt.year
df['Mes'] = df['Fecha'].dt.month
df['Día'] = df['Fecha'].dt.day
print(df)


