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
print('_'*80 + '\n' + '_'*80)

# Agrupación y Agregación de Datos
# Puedes agrupar datos por una o más columnas y luego aplicar funciones de agregación como sum, mean, etc.
print('_'*80 + '\nAgrupar por Ciudad y calcular la edad promedio_________\n' + '_'*80)
grupo_ciudad = df.groupby('Ciudad')
print(grupo_ciudad['Edad'].mean())

print('_'*50 + '\nAgrupar por Clasificación y contar el número de personas en cada grupo_________\n' + '_'*50) 
print(df.groupby('Clasificación').size())
print('_'*80 + '\n' + '_'*80)