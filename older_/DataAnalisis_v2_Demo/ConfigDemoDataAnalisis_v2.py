# acá se definen varias cosas que se van a pasar por parámetros a diferentes funciones 
# por ejemplo
# para el listado de alumnos, voy a definir las columnas que necesito visualizar
listado_de_alumnos = {
    # columnas que quiero que queden
    'cols' : [
        'DESEMPEÑO',
        'Alumno_ID',
        'Operativo',
        'CURSO_NORMALIZADO',
        'Curso',
        'División',
        'Ausente',
        'Cantidad_de_palabras',
        'Prosodia',
        'Incluido',
        'Turno',
        'Modalidad',
        'Nivel',
        'Gestión',
        'Supervisión',
        'Escuela_ID',
        'Departamento',
        'Localidad',
        'zona',
        'Regional',
        'ciclo_lectivo'
    ],
    # columnas que no voy a necesitar
    'cols_delete':[
        'separador'
    ],
    # orientación de la forma de los datos
    'orient':'records'
}