"""
Propósito y Beneficios
Organización del Código: Facilita la organización del código al dividir funcionalidades en diferentes módulos. 
Cada módulo puede encargarse de una tarea específica, como limpieza de datos, transformación de datos, validación de datos y preprocesamiento.

Acceso Simplificado: Permite importar las funciones y clases necesarias desde el paquete de manera directa, 
lo que simplifica su uso. Por ejemplo, podrías importar directamente clean_data desde el paquete principal sin necesidad de especificar el módulo completo:

from <your_package> import clean_data

Encapsulación: __all__ define explícitamente qué se exporta al usar from <package> import *, 
lo que ayuda a controlar la encapsulación y oculta detalles internos del paquete que no necesitan ser expuestos al usuario final.

Legibilidad y Mantenimiento: Hace que el código sea más legible y más fácil de mantener 
al seguir una estructura clara y predecible. Cualquier desarrollador que trabaje en el paquete 
o lo utilice puede entender rápidamente qué funcionalidades están disponibles y cómo se estructuran.

Uso del Paquete
Luego puedes utilizar tu paquete de la siguiente manera:

from your_package import clean_data, transform_data, validate_data
from your_package.preprocessor import Preprocessor

# Ejemplo de uso
data = ...

cleaned_data = clean_data(data)
transformed_data = transform_data(cleaned_data)
validated_data = validate_data(transformed_data)

preprocessor = Preprocessor()
preprocessed_data = preprocessor.preprocess(validated_data)

El archivo __init__.py en Python se utiliza para marcar directorios en el sistema de archivos como paquetes de Python. 
Cuando un directorio contiene un archivo __init__.py, se trata como un módulo de Python, 
lo que permite importar su contenido de manera más organizada y estructurada.

En el contexto de un framework de análisis de datos en Python, el contenido que has mostrado en el archivo __init__.py sirve para varios propósitos:

Estas líneas importan funciones y clases específicas 
(clean_data, transform_data, validate_data y Preprocessor) de los módulos correspondientes 
(cleaning.py, transformation.py, validation.py y preprocessor.py) dentro del mismo paquete.
"""
from .cleaning import clean_data
from .transformation import transform_data
from .validation import validate_data
from .preprocessor import Preprocessor  # Asegúrate de que esta línea esté presente y correctamente definida en preprocessing/__init__.py

"""
La variable __all__ es una lista de cadenas que define los nombres de los módulos, 
clases y funciones que serán exportados cuando se realice una importación del tipo from <package> import *. 
En este caso, solo clean_data, transform_data y validate_data serán accesibles con esta forma de importación.
"""
__all__ = ['clean_data', 'transform_data', 'validate_data']
