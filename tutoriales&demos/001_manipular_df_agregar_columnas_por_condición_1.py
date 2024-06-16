import pandas as pd

# Manipulación de DataFrames con pandas
print('_'*70 + '\nCrear un diccionario de listas________________________________________\n' + '_'*70)
data = {
    'Nombre'    : ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad'      : [28, 34, 29, 42],
    'Ciudad'    : ['Guaymallén', 'Godoy Cruz', 'San Rafael', 'San Martín']
}
# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)
print(df)

# Agregar columnas
# Puedes agregar nuevas columnas a un DataFrame basado en cálculos u otros datos.
print('_'*50 + '\nAgregar una columna que indica si la persona es mayor de 30 años_________\n' + '_'*50)
df['Mayor_de_30'] = df['Edad'] > 30
print(df)
print('_'*70 + '\n' + '_'*70)