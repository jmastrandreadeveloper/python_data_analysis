# acá se agrupan las funciones desetinadas a calcular el desempeño
import sys
from functools import reduce
import pandas as pd
from itertools import product
# la clave está en pasar los paths en done está la libreria y en donde está la demo
sys.path.insert(1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs') # acá está el config de la librería
sys.path.insert(1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs') # para linux en mi notebook !!
import libConfig as lib  # importo las referencias a la librería
import DemoPathConfigs as dPC # esto es para configurar los path internos al proyecto

import RepPython.DataAnalisis_v2_Demo.Módulos.NO_ProcessData
import Módulos.GroupData
import Módulos.CalcularDesempeño
import Módulos.HelperClass


df_FluidezLectora_1 = lib.IO.dataFetching.fetchCSV(
    dPC.carpetaDemo + r'/BasesDeEntrada/Fluidez Lectora 1.csv'
)


def agrupar(df, group_by_columns, agg_dict):
    """
    Agrupa el DataFrame df por las columnas especificadas en group_by_columns y aplica las agregaciones definidas en agg_dict.

    Parámetros:
    - df (pd.DataFrame): DataFrame a agrupar.
    - group_by_columns (list): Lista de columnas por las cuales agrupar.
    - agg_dict (dict): Diccionario que define las columnas y funciones de agregación a aplicar.

    Retorna:
    - pd.DataFrame: Resultado del agrupamiento y agregación.
    """
    grouped_df = df.groupby(group_by_columns).agg(agg_dict)
    return grouped_df




# def consulta_iterativa_no_borrar(func_construir_consulta , Escuela_ID, dFrame, lista, index_, columns_, values_, aggfunc_, sorted_, reindex_):
#     # item es el curso
#     dict_desempeño_por_curso_division = {}
#     for item in lista:
#         # Construir la consulta para el curso actual en la iteración
#         consulta_actual = func_construir_consulta(Escuela_ID, item)
#         rslt_df = dFrame.query(consulta_actual)
#         desempeño_por_curso_division_df = pd.pivot_table(
#             rslt_df,
#             index=[index_],
#             columns=columns_,
#             values=values_,
#             aggfunc=aggfunc_
#         )
#         cols = sorted(rslt_df[sorted_].unique(), reverse=False)
#         desempeño_por_curso_division_df = desempeño_por_curso_division_df.reindex(columns=cols).fillna(0).reindex(reindex_)
#         dict_desempeño_por_curso_division[item] = desempeño_por_curso_division_df
#     return dict_desempeño_por_curso_division

def consulta_itertools(func_construir_consulta, Escuela_ID, dFrame, lista_cursos, lista_sexos, rango_edades, index_, columns_, values_, aggfunc_, sorted_, reindex_):
    dict_desempeño = {}
    
    # Genera todas las combinaciones posibles de curso, sexo y rango de edad
    for curso, sexo, edad in product(lista_cursos, lista_sexos, rango_edades):
        # Construir la consulta para la combinación actual
        consulta_actual = func_construir_consulta(Escuela_ID, curso, sexo, edad)
        rslt_df = dFrame.query(consulta_actual)
        
        # Crear la tabla pivotante
        desempeño_df = pd.pivot_table(
            rslt_df,
            index=[index_],
            columns=columns_,
            values=values_,
            aggfunc=aggfunc_
        )
        
        # Ordenar las columnas, rellenar valores faltantes y reindexar
        cols = sorted(rslt_df[sorted_].unique(), reverse=False)
        desempeño_df = desempeño_df.reindex(columns=cols).fillna(0).reindex(reindex_)
        
        # Guardar el resultado usando una clave que representa la combinación de condiciones
        dict_desempeño[(curso, sexo, edad)] = desempeño_df
    
    return dict_desempeño

def construir_consulta(Escuela_ID, CURSO_NORMALIZADO , División):
    return f"(Escuela_ID == {Escuela_ID}) & (CURSO_NORMALIZADO == '{CURSO_NORMALIZADO}') & (División == '{División}')"


def consulta_iterativa(func_construir_consulta, Escuela_ID, dFrame, index_, columns_, values_, aggfunc_, sorted_, reindex_, **kwargs):
    dict_desempeño = {}
    
    # Prepara una lista de listas con las condiciones de iteración
    condiciones_iteracion = [kwargs[condicion] for condicion in kwargs]
    
    # Itera sobre todas las combinaciones posibles de las condiciones de iteración
    for valores_condiciones in product(*condiciones_iteracion):
        # Construye un diccionario con las condiciones actuales de la iteración
        condiciones = dict(zip(kwargs.keys(), valores_condiciones))
        
        # Construir la consulta para la combinación actual de condiciones
        consulta_actual = func_construir_consulta(Escuela_ID, **condiciones)
        rslt_df = dFrame.query(consulta_actual)
        
        # Crea la tabla pivotante
        desempeño_df = pd.pivot_table(
            rslt_df,
            index=[index_],
            columns=columns_,
            values=values_,
            aggfunc=aggfunc_
        )
        
        # Ordenar, rellenar, y reindexar según se necesite
        cols = sorted(rslt_df[sorted_].unique(), reverse=False)
        desempeño_df = desempeño_df.reindex(columns=cols).fillna(0).reindex(reindex_)
        
        # Usa una tupla con las condiciones como clave del diccionario
        dict_desempeño[valores_condiciones] = desempeño_df
    
    return dict_desempeño


lista = ['2°', '3°', '4°', '5°', '6°']
Escuela_ID = 9
index = 'DESEMPEÑO'
columns = 'División'
values = 'Desempeño_por_Escuela_CURSO_NORMALIZADO_Division'
aggfunc = 'first'
sorted_column = 'División'
reindex_ = ['Crítico', 'Básico', 'Medio', 'Avanzado']

dict_desempeño = consulta_iterativa(
    construir_consulta,
    Escuela_ID,
    dFrame,  # Asegúrate de que dFrame esté definido correctamente
    index,
    columns,
    values,
    aggfunc,
    sorted_column,
    reindex_,
    CURSO_NORMALIZADO = lista
)


df_FluidezLectora_1 = Módulos.NO_ProcessData.procesar_fluidez_lectora_1(df_FluidezLectora_1)

# agrupo fluidez lectora por escuela curso division departamento y localidad (probar con sexo y edad)
dFrame = agrupar(
    df_FluidezLectora_1,
    [
        'Escuela_ID',
        'CURSO_NORMALIZADO',
        'División',
        'Departamento',
        'Localidad'
    ],
    {'Alumno_ID': 'count'}
)

# desempeño
df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division_Departamento_Localidad = Módulos.CalcularDesempeño.por_escuela_curso_división_departamento_localidad(df_FluidezLectora_1)


# Asegúrate de tener definido tu DataFrame 'dFrame' antes de llamar a la función
# Llamada a la función consulta_iterativa sin pasar la consulta como argumento
dict_desempeño = consulta_iterativa(
    construir_consulta,
    Escuela_ID,
    dFrame,  # Asegúrate de que dFrame esté definido correctamente
    index,
    columns,
    values,
    aggfunc,
    sorted_column,
    reindex_,
    CURSO_NORMALIZADO = lista
)


for key, value in dict_desempeño.items():
    print(key)
    print(value)

print('....fin')



# dFrame = pd.DataFrame()

# data = """Escuela_ID;CURSO_NORMALIZADO;División;Total_Alumnos_por_Escuela_ID_CURSO_NORMALIZADO_y_División;DESEMPEÑO;Total_Alumnos_por_Tipo_de_Desempeño;Desempeño_por_Escuela_CURSO_NORMALIZADO_Division
# 9;2°;A;31;Básico;4;12.9
# 9;2°;A;31;Crítico;25;80.65
# 9;2°;A;31;Medio;2;6.45
# 9;2°;B;33;Básico;5;15.15
# 9;2°;B;33;Crítico;23;69.7
# 9;2°;B;33;Medio;5;15.15
# 9;2°;C;26;Básico;9;34.62
# 9;2°;C;26;Crítico;15;57.69
# 9;2°;C;26;Medio;2;7.69
# 9;2°;D;28;Avanzado;1;3.57
# 9;2°;D;28;Básico;3;10.71
# 9;2°;D;28;Crítico;20;71.43
# 9;2°;D;28;Medio;4;14.29
# 9;3°;A;31;Avanzado;6;19.35
# 9;3°;A;31;Básico;13;41.94
# 9;3°;A;31;Crítico;4;12.9
# 9;3°;A;31;Medio;8;25.81
# 9;3°;B;33;Avanzado;4;12.12
# 9;3°;B;33;Básico;9;27.27
# 9;3°;B;33;Crítico;16;48.48
# 9;3°;B;33;Medio;4;12.12
# 9;3°;C;27;Avanzado;4;14.81
# 9;3°;C;27;Básico;13;48.15
# 9;3°;C;27;Crítico;5;18.52
# 9;3°;C;27;Medio;5;18.52
# 9;3°;D;24;Avanzado;2;8.33
# 9;3°;D;24;Básico;8;33.33
# 9;3°;D;24;Crítico;11;45.83
# 9;3°;D;24;Medio;3;12.5
# 9;4°;A;34;Avanzado;3;8.82
# 9;4°;A;34;Básico;11;32.35
# 9;4°;A;34;Crítico;13;38.24
# 9;4°;A;34;Medio;7;20.59
# 9;4°;B;32;Avanzado;4;12.5
# 9;4°;B;32;Básico;7;21.88
# 9;4°;B;32;Crítico;8;25.0
# 9;4°;B;32;Medio;13;40.62
# 9;4°;C;22;Avanzado;1;4.55
# 9;4°;C;22;Básico;8;36.36
# 9;4°;C;22;Crítico;7;31.82
# 9;4°;C;22;Medio;6;27.27
# 9;4°;D;23;Avanzado;3;13.04
# 9;4°;D;23;Básico;6;26.09
# 9;4°;D;23;Crítico;9;39.13
# 9;4°;D;23;Medio;5;21.74
# 9;5°;A;30;Avanzado;3;10.0
# 9;5°;A;30;Básico;8;26.67
# 9;5°;A;30;Crítico;11;36.67
# 9;5°;A;30;Medio;8;26.67
# 9;5°;B;29;Avanzado;7;24.14
# 9;5°;B;29;Básico;8;27.59
# 9;5°;B;29;Crítico;9;31.03
# 9;5°;B;29;Medio;5;17.24
# 9;5°;C;27;Avanzado;2;7.41
# 9;5°;C;27;Básico;9;33.33
# 9;5°;C;27;Crítico;11;40.74
# 9;5°;C;27;Medio;5;18.52
# 9;5°;D;31;Avanzado;3;9.68
# 9;5°;D;31;Básico;8;25.81
# 9;5°;D;31;Crítico;16;51.61
# 9;5°;D;31;Medio;4;12.9
# 9;6°;A;31;Avanzado;1;3.23
# 9;6°;A;31;Básico;13;41.94
# 9;6°;A;31;Crítico;5;16.13
# 9;6°;A;31;Medio;12;38.71
# 9;6°;B;28;Avanzado;2;7.14
# 9;6°;B;28;Básico;13;46.43
# 9;6°;B;28;Crítico;4;14.29
# 9;6°;B;28;Medio;9;32.14
# 9;6°;C;29;Avanzado;6;20.69
# 9;6°;C;29;Básico;11;37.93
# 9;6°;C;29;Crítico;3;10.34
# 9;6°;C;29;Medio;9;31.03
# 9;6°;D;25;Avanzado;8;32.0
# 9;6°;D;25;Básico;4;16.0
# 9;6°;D;25;Crítico;5;20.0
# 9;6°;D;25;Medio;8;32.0
# 9;7°;A;27;Avanzado;3;11.11
# 9;7°;A;27;Básico;5;18.52
# 9;7°;A;27;Crítico;4;14.81
# 9;7°;A;27;Medio;15;55.56
# 9;7°;B;25;Avanzado;1;4.0
# 9;7°;B;25;Básico;5;20.0
# 9;7°;B;25;Crítico;7;28.0
# 9;7°;B;25;Medio;12;48.0
# 9;7°;C;26;Avanzado;5;19.23
# 9;7°;C;26;Básico;4;15.38
# 9;7°;C;26;Crítico;7;26.92
# 9;7°;C;26;Medio;10;38.46
# 9;7°;D;24;Avanzado;2;8.33
# 9;7°;D;24;Básico;6;25.0
# 9;7°;D;24;Crítico;7;29.17
# 9;7°;D;24;Medio;9;37.5
# 9;7°;E;28;Avanzado;3;10.71
# 9;7°;E;28;Básico;6;21.43
# 9;7°;E;28;Crítico;7;25.0
# 9;7°;E;28;Medio;12;42.86"""

# data_io = StringIO(data)

# Leer los datos en un DataFrame
# dFrame = pd.read_csv(data_io, sep=';')

# Utilizamos StringIO para convertir la cadena de texto multi-línea en un objeto similar a un archivo.
# Esto permite a pd.read_csv leer los datos como si vinieran de un archivo CSV.
# Parámetros de la llamada