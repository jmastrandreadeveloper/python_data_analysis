import pandas as pd

# Creación de un DataFrame desde un diccionario
# Una de las formas más comunes de crear un DataFrame es a partir de un diccionario de listas.
print('_'*50 + '\nCrear un diccionario de listas____________________\n' + '_'*50)
data = {
    'Nombre'    : ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad'      : [28, 34, 29, 42],
    'Ciudad'    : ['Guaymallén', 'Godoy Cruz', 'San Rafael', 'San Martín']
}
print(data)
# Crear un DataFrame a partir del diccionario
df = pd.DataFrame(data)
# Mostrar el DataFrame
print(df)
print('_'*50 + '\n' + '_'*50)