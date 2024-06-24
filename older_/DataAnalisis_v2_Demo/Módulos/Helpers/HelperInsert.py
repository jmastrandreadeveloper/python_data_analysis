# un ayudante que inserta los datos en donde le digamos
import sys
import os
import pandas as pd
# la clave está en pasar los paths en done está la libreria y en donde está la demo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs') # para linux en mi notebook !!
import libConfig as lib # importo las referencias a la librería

class HelperInsert:
    
    @staticmethod
    def insertar_lista_de_cursos_escuela(listDictFinal,Escuela_ID,lista_de_cursos):
        listDictFinal = lib.UTILS.utils.insert_data_into_dict(
            listDictFinal, 
            'Escuela_ID', 
            [
                'props' 
            ], 
            Escuela_ID, 
            'lista_de_cursos', 
            lista_de_cursos
        )
        return listDictFinal