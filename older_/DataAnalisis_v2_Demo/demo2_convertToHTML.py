# # esto es para configurar los path internos al proyecto

# import libConfig as lib  # importo las referencias a la librería
# import DemoPathConfigs as dPC
# import sys
# import os
# import pandas as pd
# import re
# # la clave está en pasar los paths en done está la libreria y en donde está la demo
# # acá está el config de la librería
# sys.path.insert(
#     1, 'E:\GitHub\JMastrandrea.DEVELOPER\RepPython\DataAnalisis_v2\Libs')
# # para linux en mi notebook !!
# sys.path.insert(
#     1, '/home/jorge/Documentos/GitHub/JMastrandrea.DEVELOPER/RepPython/DataAnalisis_v2/Libs')
# # leer paths específico de la demo, por ejemplo las rutas de los archivos
# ##################################################################################################################################
# # CARPETA BASE DEL PROYECTO DEMO
# # me trae toda la ruta completa en donde está el proyecto, no la librería!
# carpeta = os.path.dirname(__file__)
# ##################################################################################################################################

# el archivo a convertir
# jsonFile = lib.IO.dataFetching.leer_json(
#     dPC.carpetaDemo + r'/BasesDeSalida/9_json.json'
# )
# las configuraciones
configs = {
    'contenedor': {
        'class': 'classA classB classC',
        'style': 'styleA;styleB;styleC;styleD;',
        'slide 1': {
            'título': {
                'texto': 'Informe Operativo Fluidez Lectora 1',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'título': {
                'texto': 'id escuela',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },

            'tabla': {
                'data': {
                    'source': 'data/datos_institucionales',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;',
                    'otros estilos': 'otros estilos'
                },
                'título':
                {
                    'texto': 'matricula por curso',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'subtítulo':
                {
                    'texto': '-',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'pie_subtítulo': {
                    'texto': '-',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                }
            }

        },
        'slide 2': {
            'título': {
                'texto': 'lista de cursos de la escuela',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'lista': {
                'source': 'data/lista_de_cursos_escuela',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'título': {
                'texto': 'matrícula de la escuela',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'título': {
                'source': 'data/matricula_por_escuela',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },

            'tabla': {
                'data': {
                    'source': 'data/matricula_por_curso',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;',
                    'otros estilos': 'otros estilos'
                },
                'título':
                {
                    'texto': 'matricula por curso',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'subtítulo':
                {
                    'texto': '-',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'pie_subtítulo': {
                    'texto': '-',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                }
            }
        },
        'slide 3': {
            'título': {
                'texto': 'matricula por curso división',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'tabla': {
                'data': {
                    'source': 'data/matricula_por_curso_división',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'título':
                {
                    'texto': 'matricula por curso división',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'props': 'horizontal-scroll'
            }
        },
        'slide 4': {
            'título': {
                'texto': 'Fluidez Lectora',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'título': {
                'texto': 'matrícula examinada en fluidez lectora 1',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'título': {
                'source': 'data/fluidez lectora 1/matricula_por_escuela_fluidez_lectora_1',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'título': {
                'texto': 'lista de cursos de la escuela en Fludiez Lectora 1',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'lista': {
                'source': 'data/fluidez lectora 1/listado_de_cursos_fluidez_lectora_1',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },

            'tabla': {
                'data': {
                    'source': 'data/fluidez lectora 1/matricula_por_curso_fluidez_lectora_1',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;',
                    'otros estilos': 'otros estilos'
                },
                'título':
                {
                    'texto': 'matricula examinada por curso en fludiez lectora 1',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'subtítulo':
                {
                    'texto': '-',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'pie_subtítulo': {
                    'texto': '-',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                }
            },
            'título': {
                'texto': 'matricula examinada por curso y división en fluidez lectora 1',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'simple-layout': {
                'props': 'bullet-scroll-use-key',
                'tabla': {
                    'data': {
                        'source': 'data/fluidez lectora 1/matricula_por_curso_y_división_fluidez_lectora_1',
                        'class': 'classA classB classC',
                        'style': 'styleA;styleB;styleC;styleD;'
                    },
                    'título':
                    {
                        'texto': 'matricula por curso división',
                        'class': 'classA classB classC',
                        'style': 'styleA;styleB;styleC;styleD;'
                    }
                }
            }
        },

        'slide 5': {
            'título': {
                'texto': 'desempeño por escuela',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'pieChartJS': {
                "opcionesBarra": [
                    {
                        "responsive": True,
                        "plugins": {
                            "legend": {
                                "position": "top"
                            },
                            "title": {
                                "display": True,
                                "text": "desempeño por escuela"
                            }
                        }
                    }
                ],
                'source': 'data/fluidez lectora 1/desempeño_por_escuela',
                'pieChartJSColors': {
                    'labels': {
                        'Crítico': {'backgroundColor': 'rgba(32, 81, 89, 0.5)'},
                        'Básico': {'backgroundColor': 'rgba(48, 122, 138, 0.5)'},
                        'Medio': {'backgroundColor': 'rgba(74, 172, 174, 0.5)'},
                        'Avanzado': {'backgroundColor': 'rgba(157, 222, 220, 0.5)'}
                    }
                },
                'pieChartJSBorderColors': {
                    'labels': {
                        'Crítico': {'backgroundColor': 'rgba(10, 20, 30, 0.5)'},
                        'Básico': {'backgroundColor': 'rgba(10, 20, 30, 0.5)'},
                        'Medio': {'backgroundColor': 'rgba(10, 20, 30, 0.5)'},
                        'Avanzado': {'backgroundColor': 'rgba(10, 20, 30, 0.5)'}
                    }
                },
                'hoverOffset': 4
            },

            'tabla': {
                'data': {
                    'source': 'data/fluidez lectora 1/total_alumnos_por_escuela_fluidez_lectora_1',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'título':
                {
                    'texto': 'total de alumnos por escuela examinados en fluidez_lectora 1',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                }
            }
        },

        'slice 6': {
            'título': {
                'texto': 'desempeño por escuela y curso',
                'class': 'classA classB classC',
                'style': 'styleA;styleB;styleC;styleD;'
            },
            'barChartJS': {
                'opcionesBarra': [
                    {
                        'scales': {
                            'x': {
                                'stacked': True,
                                'grid': {
                                    'display': True
                                }
                            },
                            'y': {
                                'stacked': True,
                                'grid': {
                                    'display': True
                                }
                            }
                        },
                        'responsive': True,
                        'maintainAspectRatio': True,
                        'aspectRatio': 0.8,
                        'plugins': {
                            'legend': {
                                "position": "top"
                            },
                            'title': {
                                'display': True,
                                'text': "desempeño por escuela y curso"
                            }
                        }
                    }
                ],
                'source': 'data/fluidez lectora 1/desempeño_por_escuela_y_curso',
                'barChartJSColors': {
                    'labels': {
                        'Crítico': {'backgroundColor': 'rgba(32, 81, 89, 0.5)'},
                        'Básico': {'backgroundColor': 'rgba(48, 122, 138, 0.5)'},
                        'Medio': {'backgroundColor': 'rgba(74, 172, 174, 0.5)'},
                        'Avanzado': {'backgroundColor': 'rgba(157, 222, 220, 0.5)'}
                    }
                }
            },
            'tabla': {
                'data': {
                    'source': 'data/fluidez lectora 1/total_alumnos_por_tipo_de_desempeño_por_curso',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
                'título':
                {
                    'texto': 'total alumnos por tipo de_desempeño por curso examinados en fluidez_lectora 1',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                }
            }
        },

        'slice 7': {
            'título':
                {
                    'texto': 'desempeño por escuela curso y division en fluidez_lectora 1',
                    'class': 'classA classB classC',
                    'style': 'styleA;styleB;styleC;styleD;'
                },
            'simple-layout': {
                'props': 'bullet-scroll-use-key',
                'barChartJS': {
                    'opcionesBarra': [
                        {
                            'scales': {
                                'x': {
                                    'stacked': True,
                                    'grid': {
                                        'display': True
                                    }
                                },
                                'y': {
                                    'stacked': True,
                                    'grid': {
                                        'display': True
                                    }
                                }
                            },
                            'responsive': True,
                            'maintainAspectRatio': True,
                            'aspectRatio': 0.8,
                            'plugins': {
                                'legend': {
                                    "position": "top"
                                },
                                'title': {
                                    'display': True,
                                    'text': "desempeño por escuela curso y division en fluidez_lectora 1"
                                }
                            }
                        }
                    ],
                    'source': 'data/fluidez lectora 1/desempeño_por_escuela_curso_y_division',
                    'barChartJSColors': {
                        'labels': {
                            'Crítico': {'backgroundColor': 'rgba(32, 81, 89, 0.5)'},
                            'Básico': {'backgroundColor': 'rgba(48, 122, 138, 0.5)'},
                            'Medio': {'backgroundColor': 'rgba(74, 172, 174, 0.5)'},
                            'Avanzado': {'backgroundColor': 'rgba(157, 222, 220, 0.5)'}
                        }
                    }
                }
                }
        }
    }
}


display = {
    'contenedor': {
        'col1': {
            'filtros': [
                'filtro-por-curso',
                'filtro-por-curso-división',
            ]
        },
        'col2': {
            'sliders-container': {
                'slider-1': {
                    'fila1': {
                        'col3': {
                            'contenido1': [
                                'sample1'
                            ]
                        },
                        'col4': {
                            'contenido2': [
                                'sample2'
                            ]
                        },
                        'col5': {
                            'contenido3': [
                                'sample3'
                            ]
                        },
                        'col6': {
                            'contenido4': [
                                'sample4'
                            ]
                        }
                    },
                    'fila2': {
                        'col7': {
                            'contenido5': [
                                'sample5'
                            ]
                        },
                        'col8': {
                            'contenido6': [
                                'sample6'
                            ]
                        },
                        'col9': {
                            'col5 + col6': {
                                'contenido7': [
                                    'sample7'
                                ]
                            }
                        }
                    },
                    'fila3': {
                        'col10': {
                            'col3 + (col4 / 2) ': {
                                'contenido8': [
                                    'sample8'
                                ]
                            }
                        },
                        'col11': {
                            '(col4 / 2) + (col5 + col6)': {
                                'contenido9': [
                                    'sample9'
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
}

# el resultado
# dataSliderJSON = lib.UTILS.jsonToDataSlider.convertir_a_data_slider(
#     jsonFile,
#     configs
# )


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
