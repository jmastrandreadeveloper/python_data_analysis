# Fusión y Unión de DataFrames con pandas
# En este tutorial, aprenderás cómo combinar DataFrames 
# utilizando las funciones merge, concat y join de pandas. 
# Estas operaciones te permiten fusionar datos de diferentes 
# fuentes en un solo DataFrame para un análisis más completo.

# 1. Fusión de DataFrames con merge
# La función merge es similar a la operación SQL JOIN 
# y te permite fusionar dos DataFrames basándote en una o más claves.

import pandas as pd

print('\n')
print('Crear el primer DataFrame de ejemplo')
data1 = {
    'ID': [1, 2, 3, 4],
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta']
}
df1 = pd.DataFrame(data1)
print(df1,'\n')

print('Crear el segundo DataFrame de ejemplo')
data2 = {
    'ID': [5, 6, 7, 8],
    'Ciudad': ['Guaymallén', 'Godoy Cruz', 'San Martín', 'Lavalle']
}
df2 = pd.DataFrame(data2)
print(df2,'\n')

# Tipos de merge: inner, outer, left, right
# Puedes especificar el tipo de fusión utilizando el parámetro how.
print('Fusionar los DataFrames en la columna ID (outer)')
# Outer join (unión de todas las claves)
df_outer = pd.merge(df1, df2, on='ID', how='outer')
print(df_outer,'\n')