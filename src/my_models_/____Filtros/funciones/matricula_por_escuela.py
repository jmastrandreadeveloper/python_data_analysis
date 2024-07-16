import pandas

def matricula_por_escuela(Escuela_ID, dFrame):
    # Filtrar el DataFrame por Escuela_ID
    dFrame_filtrado = dFrame[dFrame['Escuela_ID'] == Escuela_ID]
    
    # Devolver el primer valor de Alumno_ID como entero
    if not dFrame_filtrado.empty:
        return int(dFrame_filtrado['Alumno_ID'].values[0])
    else:
        return 0  # o algún valor por defecto que prefieras, si no hay coincidencias