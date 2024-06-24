from itertools import product
import pandas as pd

def filtrar(func_construir_consulta, Escuela_ID, dFrame, index_, columns_, values_, aggfunc_, sorted_, reindex_, **kwargs):
    dict_resultados = {}
    
    # Para las condiciones de las cuales no conoces los valores de antemano, como las divisiones,
    # puedes obtener los valores únicos directamente del DataFrame:
    condiciones_desconocidas = {columna: dFrame[columna].unique() for columna in kwargs.get('condiciones_desconocidas', [])}
    
    # Combina las condiciones conocidas en kwargs con las desconocidas
    condiciones_iteracion = {**kwargs, **condiciones_desconocidas}
    valores_iteracion = [condiciones_iteracion[condicion] for condicion in condiciones_iteracion]
    
    for valores_condiciones in product(*valores_iteracion):
        condiciones = dict(zip(condiciones_iteracion.keys(), valores_condiciones))
        
        # Asegúrate de excluir las 'condiciones_desconocidas' de las condiciones pasadas a construir_consulta
        condiciones_filtradas = {k: v for k, v in condiciones.items() if k not in ['condiciones_desconocidas']}
        consulta_actual = func_construir_consulta(Escuela_ID, **condiciones_filtradas)
        rslt_df = dFrame.query(consulta_actual)
        
        resultado_df = pd.pivot_table(
            rslt_df,
            index=[index_],
            columns=columns_,
            values=values_,
            aggfunc=aggfunc_
        )
        
        if sorted_ in rslt_df:
            cols = sorted(rslt_df[sorted_].unique(), reverse=False)
            resultado_df = resultado_df.reindex(columns=cols).fillna(0).reindex(reindex_)
        
        dict_resultados[valores_condiciones] = resultado_df
    
    return dict_resultados