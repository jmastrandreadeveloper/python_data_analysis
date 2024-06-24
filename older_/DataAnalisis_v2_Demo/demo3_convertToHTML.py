# esta versión va a incluir partes del json obtenido dentro del diccionario que especifiquemos nosotros
# debemos poderr leer el json..

# leer los datos 
# los contenidos pueden ser variables.. depende de cada reporte
# en escencia todos tienen la misma estructura de datos pero pueden diferir 
# en la cantidad de cosas a mostrar.. más cursos menos cursos mas o menos divisiones.. etc
# lo otro importante será la manera en que pueda identificar cada cosa en los formatos de los datos
# para ello los datos deberán tener una consistencia para no alterar el funcionamiento del parseo 
# de la información...
# se deberá definir un diccionario que permita tener palabras claves para definir cada cosa
# por ejemplo : 'título' hará referencia a un texto que será usado para un título 'párrafo' para especificar un párrafo..
# 'tabla' para dibujar una tabla..etc



display2 = {
    'styles': {
        'style1': {'background-color': '#f8d7da', 'padding': '10px'},
        'style2': {'background-color': '#d1ecf1', 'padding': '10px'},
        'style3': {'background-color': '#d4edda', 'border': '1px solid #c3e6cb', 'padding': '0px'},
        'style4': {'padding': '10px'},
    },

    'content': {
        'row1': {
            'height': '100%',
            'col1': {
                'content': 'contenido1',
                'width': '20%',
                'style_ref': 'style1'
            },
            'col2': {
                'content': {
                    'row2': {
                        'height': '10%',
                        'col3': {
                            'content': 'contenidoA',
                            'width': '100%',
                            'style_ref': 'style2'
                        }
                    },
                    'row3': {
                        'height': '10%',
                        'col3': {
                            'content': 'contenido2',
                            'width': '25%',
                            'style_ref': 'style2'
                        },
                        'col4': {
                            'content': 'contenido3',
                            'width': '25%',
                            'style_ref': 'style4'
                        },
                        'col5': {
                            'content': 'contenido4',
                            'width': '25%',
                            'style_ref': 'style4'
                        },
                        'col6': {
                            'content': 'contenido5',
                            'width': '25%',
                            'style_ref': 'style4'
                        },
                    },
                    'row4': {
                        'height': '20%',
                        'col7': {
                            'content': 'contenido6',
                            'width': '25%',
                            'style_ref': 'style4'
                        },
                        'col8': {
                            'content': 'contenido7',
                            'width': '25%',
                            'style_ref': 'style4'
                        },
                        'col9': {
                            'content': 'contenido8',
                            'width': '50%',
                            'style_ref': 'style4'
                        },
                    },
                    'row5': {
                        'height': '60%',
                        'col10': {
                            'content': 'contenido9',
                            'width': '40%',
                            'style_ref': 'style4'
                        },
                        'col11': {
                            'content': 'contenido10',
                            'width': '60%',
                            'style_ref': 'style4'
                        },
                    },
                },
                'width': '80%',
                'style_ref': 'style3'
            }
        }
    }
}

def dict_to_html(display, styles_dict=None, level=0):
    html_content = ""
    if level == 0:  # Solo entra aquí en el nivel más alto
        styles_dict = display.get('styles', {})
        content = display.get('content', {})
        return dict_to_html(content, styles_dict, level + 1)
    else:
        if isinstance(display, dict):
            for key, value in display.items():
                styles = ""
                if "col" in key or "row" in key:
                    content = value.get('content', value) if isinstance(value, dict) else value
                    width = value.get('width', 'auto') if isinstance(value, dict) else 'auto'
                    height = value.get('height', 'auto') if "row" in key and isinstance(value, dict) else 'auto'
                    style_ref = value.get('style_ref', None)
                    additional_styles = styles_dict.get(style_ref, {}) if style_ref else {}

                    if width != 'auto':
                        styles += f"flex: 0 0 {width}; max-width: {width};"
                    if height != 'auto':
                        styles += f"height: {height};"
                    for style_key, style_value in additional_styles.items():
                        styles += f"{style_key}: {style_value}; "

                    default_styles = "padding: 10px; border: 1px solid #ccc;" if "col" in key else "display: flex; flex-wrap: wrap; margin-bottom: 10px;"
                    styles += default_styles

                    class_attr = "row" if "row" in key else "col"
                    html_content += f'<div class="{class_attr}" style="{styles}">\n'
                    if isinstance(content, dict):
                        html_content += dict_to_html(content, styles_dict, level + 1)
                    else:
                        html_content += f'<p>{content}</p>'
                    html_content += '</div>\n'
        elif isinstance(display, list):
            for item in display:
                html_content += dict_to_html(item, styles_dict, level + 1)
        else:
            html_content += f'<p>{display}</p>\n'
    
    return html_content




html_output = dict_to_html(display2)

html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualización de Diccionario</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        html, body {{
            height: 100%; /* Hace que el html y body ocupen el 100% de la altura de la pantalla */
            margin: 0;
            padding: 0; /* Remueve el padding por defecto */
            overflow: hidden; /* Opcional: Evita el desbordamiento */
        }}
        .container-fluid {{
            height: 100%; /* Hace que el contenedor ocupe el 100% de la altura disponible */
            display: flex;
            flex-direction: column;
            justify-content: stretch; /* Alinea los elementos para que se estiren en el contenedor */
            align-items: stretch; /* Alinea los elementos para que se estiren en el contenedor */
        }}
        div[class^="row"], div[class*=" row"] {{
            display: flex;
            flex-wrap: wrap;
            width: 100%; /* Asegura que las filas ocupen el 100% del ancho del contenedor */
            margin-right: 0;
            margin-left: 0;
            flex-grow: 1; /* Permite que las filas crezcan para ocupar el espacio disponible */
        }}
        div[class^="col"], div[class*=" col"] {{
            position: relative;
            flex-grow: 1; /* Permite que las columnas crezcan para ocupar el espacio disponible */
            padding: 0; /* Ajusta el padding según tus necesidades */
        }}
    </style>
</head>
<body>
    <div class="container-fluid">
        {html_output}
    </div>
</body>
</html>"""



print(html_template)
