import pandas as pd
from itertools import combinations
import types


def obtener_valores_unicos_columnas_iterables(dataframe, columnas_excluir=None):
    if columnas_excluir is None:
        columnas_excluir = []

    # Verificar si la columna principal está en el índice y resetear el índice si es necesario
    columnas_indices = set(dataframe.index.names)
    columnas_a_resetear = columnas_indices.intersection(set(columnas_excluir))
    if columnas_a_resetear:
        dataframe.reset_index(inplace=True)

    resultados = {}

    for columna in dataframe.columns:
        # Excluir columnas específicas de la revisión
        if columna in columnas_excluir:
            continue

        # Considerar una columna como iterable si tiene más de un valor único
        if len(dataframe[columna].unique()) > 1:
            # Almacenar los valores únicos de las columnas iterables
            resultados[columna] = dataframe[columna].unique().tolist()

    return resultados

from itertools import combinations

def generar_plantillas_de_consultas(escuela_id_nombre, columnas_iterables):
    metodos_estaticos = []

    # Generar el método estático para la consulta básica que solo contiene Escuela_ID
    metodo_basico = f"""@staticmethod
def filtrar_por_{escuela_id_nombre.lower()}({escuela_id_nombre}):
    return f"({escuela_id_nombre} == {{{{{escuela_id_nombre}}}}})\""""
    metodos_estaticos.append(metodo_basico)

    # Ahora, generar métodos estáticos que incluyen combinaciones de columnas iterables
    for r in range(1, len(columnas_iterables) + 1):
        for combo in combinations(columnas_iterables, r):
            # Generar nombres de parámetros para el método
            parametros_metodo = ', '.join([escuela_id_nombre] + list(combo))
            nombre_metodo = f"filtrar_por_{escuela_id_nombre.lower()}_y_{'_y_'.join(combo).lower()}"

            # Construir la cadena de consulta
            condiciones = [f"({escuela_id_nombre} == {{{{{escuela_id_nombre}}}}})"] + \
                          [f"({col} == '{{{{ {col} }}}}')".format(col=col) for col in combo]
            consulta = " & ".join(condiciones)

            # Construir la definición completa del método
            definicion_metodo = f"""@staticmethod
def {nombre_metodo}({parametros_metodo}):
    return f"{consulta}" """
            metodos_estaticos.append(definicion_metodo)

    return metodos_estaticos



def generar_diccionario_de_funciones(escuela_id_nombre, columnas_iterables):
    funciones_de_consultas = {}

    # Función para generar el nombre de la función
    def generar_nombre_de_funcion(combo):
        partes = [escuela_id_nombre] + list(combo)
        return 'filtrar_por_' + '_y_'.join(partes).lower()

    # Función para generar el cuerpo de la función
    def generar_funcion(consulta):
        def funcion(**kwargs):
            return consulta.format(**kwargs)
        return funcion

    # Incluir la consulta más básica que solo contiene Escuela_ID
    consulta_basica = f"({escuela_id_nombre} == {{{escuela_id_nombre}}})"
    nombre_basico = generar_nombre_de_funcion([])
    funciones_de_consultas[nombre_basico] = generar_funcion(consulta_basica)

    # Ahora, generar consultas que incluyen combinaciones de columnas iterables
    for r in range(1, len(columnas_iterables) + 1):
        for combo in combinations(columnas_iterables, r):
            condiciones = [consulta_basica] + [f"({col} == '{{{col}}}')" for col in combo]
            consulta = " & ".join(condiciones)
            nombre_de_funcion = generar_nombre_de_funcion(combo)
            funciones_de_consultas[nombre_de_funcion] = generar_funcion(consulta)

    return funciones_de_consultas

def generar_funciones_de_filtrado(escuela_id_nombre, columnas_iterables):
    funciones = {}

    def crear_funcion(nombre_funcion, columnas):
        # Generar los parámetros de la función y la cadena de consulta
        parametros = ', '.join(columnas)
        condiciones = ' & '.join([f"({col} == '{{{col}}}')"
                                  for col in columnas])
        # Crear el cuerpo de la función
        cuerpo_funcion = f"def {nombre_funcion}({parametros}):\n" \
                         f"    return f\"{condiciones}\"\n"
        # Crear un espacio de nombres local para ejecutar el cuerpo_funcion
        local_namespace = {}
        exec(cuerpo_funcion, globals(), local_namespace)
        # Extraer la función del espacio de nombres local
        return local_namespace[nombre_funcion]

    # Incluir la consulta más básica que solo contiene Escuela_ID
    nombre_basico = f"filtrar_por_{escuela_id_nombre.lower()}"
    funciones[nombre_basico] = crear_funcion(nombre_basico, [escuela_id_nombre])

    # Generar funciones para combinaciones de columnas iterables
    for r in range(1, len(columnas_iterables) + 1):
        for combo in combinations(columnas_iterables, r):
            nombre_funcion = f"filtrar_por_{escuela_id_nombre.lower()}_y_{'_y_'.join(combo).lower()}"
            funciones[nombre_funcion] = crear_funcion(nombre_funcion, [escuela_id_nombre] + list(combo))

    return funciones




def generar_consultas_para_dataframe(escuela_id, resultados_iterables):
    consultas = []
    # Generar todas las combinaciones posibles de valores iterables
    from itertools import product

    # Obtener los nombres de las columnas iterables y sus valores únicos
    nombres_columnas = list(resultados_iterables.keys())
    valores_unicos = [resultados_iterables[columna] for columna in nombres_columnas]

    # Generar combinaciones de valores únicos
    for combinacion in product(*valores_unicos):
        condiciones = [f"(Escuela_ID == {escuela_id})"]
        # Crear condiciones basadas en las combinaciones de valores únicos
        for nombre_columna, valor in zip(nombres_columnas, combinacion):
            if isinstance(valor, str):
                condiciones.append(f"({nombre_columna} == '{valor}')")
            else:
                condiciones.append(f"({nombre_columna} == {valor})")
        # Unir las condiciones para formar una consulta y agregarla a la lista de consultas
        consulta = " & ".join(condiciones)
        consultas.append(consulta)

    return consultas



"""
# Ejemplo de uso:
dataframe = pd.DataFrame({
    'CURSO_NORMALIZADO': ['1°', '2°', '3°', '1°', '2°', '3°'],
    'NOTA': [10, 9, 8, 10, 10, 9],
    'AÑO': [2021, 2021, 2021, 2022, 2022, 2022],
})

indices_a_examinar = ['CURSO_NORMALIZADO', 'NOTA', 'AÑO']
columnas_a_excluir = ['AÑO']

resultado = identificar_y_extraer_columnas(dataframe, indices_a_examinar, columnas_a_excluir)
print(resultado)
"""

class FiltradoDinamico:
    pass

def agregar_funcion_a_clase(nombre_funcion, parametros, condiciones):
    # Definir el cuerpo de la función como un método estático
    @staticmethod
    def metodo_dinamico(**kwargs):
        return condiciones.format(**kwargs)
    
    # Agregar el método estático a la clase FiltradoDinamico con el nombre especificado
    setattr(FiltradoDinamico, nombre_funcion, metodo_dinamico)

def generar_metodos_de_filtrado(escuela_id_nombre, columnas_iterables):
    # Incluir la consulta más básica que solo contiene Escuela_ID
    condiciones_basica = f"({escuela_id_nombre} == {{{escuela_id_nombre}}})"
    nombre_basico = f"filtrar_por_{escuela_id_nombre.lower()}"
    agregar_funcion_a_clase(nombre_basico, [escuela_id_nombre], condiciones_basica)

    # Generar funciones para combinaciones de columnas iterables
    for r in range(1, len(columnas_iterables) + 1):
        for combo in combinations(columnas_iterables, r):
            nombre_funcion = f"filtrar_por_{escuela_id_nombre.lower()}_y_{'_y_'.join(combo).lower()}"
            parametros = ', '.join([escuela_id_nombre] + list(combo))
            condiciones = ' & '.join([f"({col} == '{{{col}}}')"
                                      for col in [escuela_id_nombre] + list(combo)])
            agregar_funcion_a_clase(nombre_funcion, parametros, condiciones)



def integrar_metodos_en_clase(clase, escuela_id_nombre, columnas_iterables):
    def generar_metodo(consulta):
        # Esta función ahora genera una función adecuada para ser usada como método estático
        def funcion_dinamica(**kwargs):
            return consulta.format(**kwargs)
        return funcion_dinamica

    # Generar el método estático para la consulta básica que solo contiene Escuela_ID
    consulta_basica = f"({escuela_id_nombre} == {{{{{escuela_id_nombre}}}}})"
    metodo_basico = generar_metodo(consulta_basica)
    setattr(clase, f'filtrar_por_{escuela_id_nombre.lower()}', staticmethod(metodo_basico))

    # Generar métodos estáticos que incluyen combinaciones de columnas iterables
    for r in range(1, len(columnas_iterables) + 1):
        for combo in combinations(columnas_iterables, r):
            nombre_metodo = f"filtrar_por_{escuela_id_nombre.lower()}_y_{'_y_'.join(combo).lower()}"
            condiciones = [f"({escuela_id_nombre} == {{{{{escuela_id_nombre}}}}})"] + \
                          [f"({col} == '{{{{ {col} }}}}')".format(col=col) for col in combo]
            consulta = " & ".join(condiciones)
            metodo = generar_metodo(consulta)
            setattr(clase, nombre_metodo, staticmethod(metodo))

# Definir una clase de ejemplo donde se integrarán los métodos
class ConsultasDinamicas:
    pass




columnas_a_excluir = [
    'DESEMPEÑO',
    'Escuela_ID',
    'Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División',
    'Total_Alumnos_por_Tipo_de_Desempeño',
    'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'
    ]

resultados = lib.DATA.FILTER.análisis.obtener_valores_unicos_columnas_iterables(
    df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division, 
    columnas_excluir=columnas_a_excluir)

print("Valores únicos de columnas iterables:")

for columna, valores in resultados.items():
    print(f"{columna}")
    print(f"{valores}")

#### comprobar las posibles querys 
# # Supongamos que tienes un valor específico para Escuela_ID
# escuela_id_especifico = 9
# # Y supongamos que ya obtuviste los resultados de la función anterior para columnas iterables
# resultados_iterables = {
#     'CURSO_NORMALIZADO': ['2°', '3°', '4°'],
#     'División': ['A', 'B', 'C', 'D']
# }
# consultas = lib.DATA.FILTER.análisis.generar_consultas_para_dataframe(escuela_id_especifico, resultados_iterables)

# # Mostrar las consultas generadas
# for consulta in consultas:
#     print(f"{consulta};")

# Nombres de las columnas iterables
columnas_iterables =  list(resultados.keys()) #['CURSO_NORMALIZADO', 'División']
# Nombre del identificador de la escuela
escuela_id_nombre = 'Escuela_ID'
# Generar plantillas de consultas
plantillas_metodos = lib.DATA.FILTER.análisis.generar_plantillas_de_consultas(escuela_id_nombre, columnas_iterables)

# Mostrar plantillas
for plantilla in plantillas_metodos:
    print(plantilla, "\n")

print('-' * 150)    

lib.DATA.FILTER.análisis.integrar_metodos_en_clase(
    lib.DATA.FILTER.análisis.ConsultasDinamicas, 
    escuela_id_nombre, 
    columnas_iterables
)

# Ejemplo de cómo llamar a uno de los métodos agregados dinámicamente
print(lib.DATA.FILTER.análisis.ConsultasDinamicas.filtrar_por_escuela_id(Escuela_ID=123))
print(lib.DATA.FILTER.análisis.ConsultasDinamicas.filtrar_por_escuela_id_y_curso_normalizado_y_división(
    Escuela_ID=123,
    CURSO_NORMALIZADO="Matemáticas", División="A"))

dictio = {
    'filtrar_por_escuela_id' : f"(Escuela_ID == {{Escuela_ID}})",
    'filtrar_por_escuela_id_y_curso_normalizado' : f"(Escuela_ID == {{Escuela_ID}}) & (CURSO_NORMALIZADO == {{CURSO_NORMALIZADO}})",
    'filtrar_por_escuela_id_y_división' : f"(Escuela_ID == {{Escuela_ID}}) & (División == '{{División}}')",
    'filtrar_por_escuela_id_y_curso_normalizado_y_división'  : f"(Escuela_ID == {{Escuela_ID}}) & (CURSO_NORMALIZADO == '{{CURSO_NORMALIZADO}}') & (División == '{{División}}')"
}



# # Generar el diccionario de funciones
# diccionario_de_funciones = lib.DATA.FILTER.análisis.generar_diccionario_de_funciones(escuela_id_nombre, columnas_iterables)

# # Ejemplo de cómo acceder a una función específica y usarla
# nombre_de_funcion = 'filtrar_por_escuela_id_y_curso_normalizado_y_división'
# if nombre_de_funcion in diccionario_de_funciones:
#     funcion_especifica = diccionario_de_funciones[nombre_de_funcion]
#     consulta = funcion_especifica(Escuela_ID=1, CURSO_NORMALIZADO='Matemáticas', División='A')
#     print(consulta)


# print('-' * 150) 


# # Generar funciones
# funciones_de_filtrado = lib.DATA.FILTER.análisis.generar_funciones_de_filtrado(escuela_id_nombre, columnas_iterables)

# # Acceder a una función específica y ejecutarla
# funcion_especifica_nombre = 'filtrar_por_escuela_id_y_curso_normalizado_y_división'
# if funcion_especifica_nombre in funciones_de_filtrado:
#     funcion_especifica = funciones_de_filtrado[funcion_especifica_nombre]
#     consulta = funcion_especifica(Escuela_ID='1', CURSO_NORMALIZADO='Matemáticas', División='A')
#     print(consulta)

# Generar métodos de filtrado
# lib.DATA.FILTER.análisis.generar_metodos_de_filtrado(escuela_id_nombre, columnas_iterables)

# # Ejemplo de cómo llamar a uno de los métodos generados
# consulta = lib.DATA.FILTER.análisis.FiltradoDinamico.filtrar_por_escuela_id_y_curso_normalizado_y_división(
#     Escuela_ID=1, 
#     CURSO_NORMALIZADO='Matemáticas', 
#     División='A')
# print(consulta)

exit()

