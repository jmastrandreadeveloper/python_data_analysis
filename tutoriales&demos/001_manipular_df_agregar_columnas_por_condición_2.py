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
# Aplicar funciones
# Puedes aplicar funciones a las columnas o filas de un DataFrame utilizando apply.
print('_'*50 + '\nDefinir una función que clasifica edades_________\n' + '_'*50)
def clasificar_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad < 40:
        return 'Adulto'
    else:
        return 'Mayor'

# Aplicar la función a la columna 'Edad'
df['Clasificación'] = df['Edad'].apply(clasificar_edad)
print(df)
print('_'*70 + '\n' + '_'*70)