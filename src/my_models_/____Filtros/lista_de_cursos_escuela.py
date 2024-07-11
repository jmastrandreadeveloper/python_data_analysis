import pandas as pd

def lista_de_cursos_escuela( Escuela_ID , dFrame ,):
    # Reset index para poder filtrar por 'Escuela_ID'
    agrupado_reset = dFrame.reset_index()
    # Filtramos por una 'Escuela_ID' específica
    dFrame_filtrado = agrupado_reset[agrupado_reset['Escuela_ID'] == Escuela_ID]
    # busco solamente la columna 'CURSO_NORMALIZADO'
    lista_df = dFrame_filtrado['CURSO_NORMALIZADO']
    # convieto ese df de una columna a una lista
    lista_de_cursos = lista_df.to_list()
    # saco los cursos repetidos
    lista_de_cursos = list(set(lista_de_cursos))
    # y la ordeno
    lista_de_cursos.sort()
    return lista_de_cursos