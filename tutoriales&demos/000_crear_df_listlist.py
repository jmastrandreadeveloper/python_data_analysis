import pandas as pd

# Creación de un DataFrame desde una lista de listas
# Puedes crear un DataFrame a partir de una lista de listas especificando las etiquetas de las columnas.
print('_'*50 + '\nCrear una lista de listas_________________________\n' + '_'*50)
data = [
    ['Ana', 28, 'Guaymallén'],
    ['Luis', 34, 'Godoy Cruz'],
    ['Carlos', 29, 'San Rafael'],
    ['Marta', 42, 'San Martín']
]

# Crear un DataFrame a partir de la lista de listas
df = pd.DataFrame(data, columns=['Nombre', 'Edad', 'Ciudad'])
# Mostrar el DataFrame
print(df)
print('_'*50 + '\n' + '_'*50)