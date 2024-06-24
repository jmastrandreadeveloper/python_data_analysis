from src.utils import obtener_datos_de_columna

class ReporteFluidezLectora_1_PorEscuela:

    def __init__(self,df_nominal_validated,df_FL_1):
        self.df_nominal_validated = df_nominal_validated
        self.df_FL_1 = df_FL_1

    # desde acá voy a armar los archivos .json para cada escuela
    def hacer_reporte_por_lista_de_escuelas(self):
        self.Escuelas_IDs = obtener_datos_de_columna(
            self.df_nominal_validated, 
            'Escuela_ID',
            True
        )
        # listDictFinal será una lista de diccionarios, 
        # cada diccionario en la lista listDictFinal tendrá los datos de la escuela y 
        # todos los datos filtrados de fluidez lectora
        # esa lista se podrá recorrer para poder sacar luego los datos de la escuela 
        # que nosostros queramos...
        # cada uno de los diccionarios que va a mantener dentro va a tener como clave 
        # el id de la escuela..
        listDictFinal = []
        dictDatos = {
            'Escuela_ID' : None,
            'datos institucionales' : None
        }

        return self.Escuelas_IDs