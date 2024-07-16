import pandas as pd
    
def lista_de_cursos_escuela(Escuela_ID, dFrame):
    # Filtrar el DataFrame por Escuela_ID
    dFrame_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]
    
    # Devolver una lista ordenada y sin duplicados de CURSO_NORMALIZADO
    if not dFrame_filtrado.empty:
        # Aplanar la lista de cursos normalizados
        cursos = dFrame_filtrado['CURSO_NORMALIZADO'].explode().tolist()
        # Eliminar duplicados y ordenar la lista
        cursos = sorted(set(cursos))
        return cursos
    else:
        return None  # o algún valor por defecto que prefieras, si no hay coincidencias