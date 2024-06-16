import pandas as pd

# Creación de un DataFrame desde una lista de diccionarios
# Otra forma de crear un DataFrame es a partir de una lista de diccionarios.
print('_'*50 + '\nCrear una lista de diccionarios___________________\n' + '_'*50)
data = [
    {'Nombre': 'Ana', 'Edad': 28, 'Ciudad': 'Guaymallén'},
    {'Nombre': 'Luis', 'Edad': 34, 'Ciudad': 'Godoy Cruz'},
    {'Nombre': 'Carlos', 'Edad': 29, 'Ciudad': 'San Rafael'},
    {'Nombre': 'Marta', 'Edad': 42, 'Ciudad': 'San Martín'}
]
# Crear un DataFrame a partir de la lista de diccionarios
df = pd.DataFrame(data)
# Mostrar el DataFrame
print(df)
print('_'*50 + '\n' + '_'*50)