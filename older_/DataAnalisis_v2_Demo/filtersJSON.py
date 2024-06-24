# esta función lo que va a hacer es la de poder crear los filtros
# para poder navegar en la visualización de los datos del informe
# la idea es que a partir del json que le suministramos pueda crear
# un objeto filtro o varios objetos filtros para que pueda devolver
# a su vez otro objeto que mantiene todos los datos a visualizar
# y que además con el formato del layout a mostrar.. es decir
# teniendo los filtros y los layout para definidos para cada muestra
# devulve un objeto que se usará para fabricar el tablero...
# se deberá tener en cuenta algunas reglas para que armar el filtro 
# por ejemplo el filtro está definido dentro del json por ejemplo
# curso o curso división..en el caso de curso-división se tendrá
# un diccionario donde la clave es el curso y tendrá una lista de divisiones
# de esa manera se puede crear el filtro, si es solamente por curso, se 
# tendrá una lista de cursos...
# cuando se hacen los diferentes agrupamientos con los datos ese es un 
# buen momento para poder crear los objetos filtros dado que siguiendo
# la linea de los filtrados de los datos, usamos la misma lógica para
# estructurar el filtro con los datos, o sea mirando los disitintos filtros
# que hice con los datos entonces debo emplear la misma lógica que para
# armar los objetos filtros...
# filtros que se crearon:
#   -por escuela
#   -por escuela y curso
#   -por escuela-curso y división
#   -por nivel y curso
#   -por supervisión y curso
#   -por curso-supervisión y nivel
#
# habrá un tipo de layout para cada filtro, los objetos filtros van a 
# ir llamando a esos layouts para ser dibujados...
# algunos filtros, la mayoría, se pueden construir a partir de otros datos 
# ya presentes en el json...

# CONSTRUIR UN JSON QUE REPRESENTE A LOS LAYOUTS QUE SE VAN A MOSTRAR

import DemoPathConfigs as dPC
import sys
import os
import pandas as pd
import re
# la clave está en pasar los paths en done está la libreria y en donde está la demo
# acá está el config de la librería
sys.path.insert(
    1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs')
# para linux en mi notebook !!
sys.path.insert(
    1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs')
import libConfig as lib  # importo las referencias a la librería
# leer paths específico de la demo, por ejemplo las rutas de los archivos
##################################################################################################################################
# CARPETA BASE DEL PROYECTO DEMO
# me trae toda la ruta completa en donde está el proyecto, no la librería!
carpeta = os.path.dirname(__file__)
##################################################################################################################################

#el archivo a convertir
datos_json = lib.IO.dataFetching.leer_json(
    dPC.carpetaDemo + r'/BasesDeSalida/9_json.json'
)

# defino los objetos filtros y de donde deben salir
def_filtros = {
    'por_escuela' : {}
}


#################################### USAR CSSUTILS DE PYTHON PARA SIMPLIFICAR LA DEFINICION DE LOS ESTILOS DE LOS COMPONENTES ##################################

estilos = {
    '.titulo-resaltado': {
        'font-weight': 'bold',
        'font-style': 'italic',
    }
}

content_datos_institucionales = {    
    'contenedor1': [
        {
            'titulo':{
                'texto': 'Informe Operativo Fluidez Lectora 1'
            }
        },
        {
            'titulo':{                
                'texto': lib.UTILS.utils.getVal(datos_json,'id')
            }
        },
        {
            'titulo':{                
                'texto': 'id escuela'
            }            
        },
        {
            'titulo':{                
                'texto': lib.UTILS.utils.getVal(datos_json,'data/datos_institucionales/Nivel')
            }
        },
        {
            'título':{
                'texto': '<span class="titulo-resaltado">matricula de la escuela :</span>' + str(lib.UTILS.utils.getVal(datos_json,'data/matricula_por_escuela'))
            } 
        },
        {
            'título':{
                'texto': lib.UTILS.utils.getVal(datos_json,'data/matricula_por_escuela')
            }
        }
    ]
}

def convertir_estilos_a_css(estilos_dict):
    css = '<style>\n'
    for selector, propiedades in estilos_dict.items():
        css += selector + ' {\n'
        for propiedad, valor in propiedades.items():
            css += f'    {propiedad}: {valor}\n'
        css += '}\n'
    css += '</style>'
    return css

css_estilos = convertir_estilos_a_css(estilos)

# Suponiendo que lib.UTILS.utils.getVal(datos_json, 'data/matricula_por_escuela') devuelve un valor para usar
valor_matricula = str(lib.UTILS.utils.getVal(datos_json, 'data/matricula_por_escuela'))

# Construye el HTML, incluyendo los estilos y el texto con el span aplicando la clase
html_texto = css_estilos + '<div><span class="titulo-resaltado">matricula de la escuela :</span> ' + valor_matricula + '</div>'

print(html_texto)


print(content_datos_institucionales)