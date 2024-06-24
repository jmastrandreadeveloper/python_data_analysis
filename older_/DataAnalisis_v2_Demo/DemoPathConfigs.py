# acá definimos las rutas para todas las
# carpetas en donde está la librería
# además las carpetas adicionales para
# guardar imágenes, tipografías, templates, etc.
import sys
import os

# print('Nombre del archivo:', os.path.basename(__file__))
# print('Nombre del directorio:', os.path.dirname(__file__))

# # Para obtener la ruta absoluta del directorio donde se encuentra el script
# ruta_absoluta_directorio = os.path.abspath(os.path.dirname(__file__))
# print('Ruta absoluta del directorio:', ruta_absoluta_directorio)

# linux casa
#sys.path.insert(1, 'F:\ProyectosPython\ProyectoBase\configuración')
# windows trabajo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs')
############# RUTAS DE CARPETAS ####################################################################################################################################################################
carpetaDemo         = os.path.dirname(__file__) # me trae toda la ruta completa en donde está el proyecto, no la librería!
######### acá puedo definir las carpetas de salida y otras cosas