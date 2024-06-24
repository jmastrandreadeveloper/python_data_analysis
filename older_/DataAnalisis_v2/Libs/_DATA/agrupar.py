
def agrupar_por_criterio(dFrame , listaDeColumnas , agg_dict , reset_index):
    # esta función lo que va a hacer es agrupar un dataframe usando diferentes criterios,
    # el dFrame no está agrupado, en la lista de columnas están los criterios para agrupar
    # el agg_dict es la función matemática que vamos a usar en este caso siempre es count..
    # y el reset_index es un boolean que me va a indicar si necesito resetear el índice o no
    # esto sirve para cuando tenga que calcular los desempeños con dataframe que ya se han agrupado    
    dFrame.reset_index(drop=True, inplace=True)
    if reset_index :
        agrupado = dFrame.groupby(listaDeColumnas).agg(agg_dict).reset_index()
    else:
        agrupado = dFrame.groupby(listaDeColumnas).agg(agg_dict)
    return agrupado