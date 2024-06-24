"""
define una clase Analyzer que se utiliza para realizar análisis de datos, 
incluyendo la generación de histogramas y el cálculo de estadísticas descriptivas. 
A continuación, te explico en detalle lo que hace cada parte del código:

matplotlib.pyplot: Es una colección de funciones en matplotlib 
que hace que matplotlib funcione como MATLAB. 
Se utiliza para crear gráficos en Python.
seaborn: Es una librería para la visualización estadística basada en matplotlib. 
Proporciona una interfaz de alto nivel para dibujar gráficos atractivos y estadísticamente informativos.

class Analyzer: Define una nueva clase llamada Analyzer.
def __init__(self, data): Es el método constructor de la clase que se ejecuta 
cuando se crea una instancia de Analyzer. Este método toma un argumento data 
(un DataFrame de pandas, generalmente) y lo asigna al atributo self.data.

plot_histogram(self, column): Este método toma el nombre de una columna 
como argumento y genera un histograma para esa columna utilizando seaborn.
plt.figure(figsize=(10, 6)): Configura el tamaño de la figura para el histograma.
sns.histplot(self.data[column]): Utiliza seaborn para crear el histograma de los datos 
en la columna especificada.
plt.show(): Muestra el gráfico generado.


calculate_statistics(self): Este método calcula y devuelve las estadísticas descriptivas 
del DataFrame almacenado en self.data.
self.data.describe(): Llama al método describe() de pandas, 
que genera un resumen de las estadísticas descriptivas de las columnas numéricas del DataFrame, 
incluyendo la cuenta, media, desviación estándar, valores mínimo y máximo, y los percentiles.
"""

import matplotlib.pyplot as plt
import seaborn as sns

class Analyzer:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column])
        plt.show()

    def calculate_statistics(self):
        return self.data.describe()
