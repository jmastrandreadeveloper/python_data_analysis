import os
import pandas as pd

# Ruta de la carpeta donde están las clases concretas
base_path = os.path.dirname(os.path.abspath(__file__))
concrete_models_path = os.path.join(base_path, 'src/my_models_/fluidez_lectora_1')

# Función para generar una nueva clase GroupData con métodos de agrupamiento
def generate_group_data_class(group_params_list, output_dir):
    concrete_models_path = os.path.join(output_dir)
    os.makedirs(concrete_models_path, exist_ok=True)

    class_content = ""
    
    class_content += "import pandas as pd\n\n"
    
    # Generar la clase GroupData dinámicamente
    class_content += "class GroupData:\n"
    class_content += "    def __init__(self, dataframe: pd.DataFrame):\n"
    class_content += "        self.dataframe = dataframe\n\n"
    
    # Generar métodos de agrupamiento
    for columns, agg_dict, options in group_params_list:
        method_name = generate_method_name(columns, agg_dict)
        method_content = generate_group_method_content(columns, agg_dict, options)
        class_content += method_content

    # Guardar la clase GroupData en un archivo .py
    group_data_file = os.path.join(concrete_models_path, 'GroupData.py')
    with open(group_data_file, 'w', encoding='utf-8') as f:  # Especificar la codificación UTF-8
        f.write(class_content)

    print(f"Clase GroupData generada exitosamente en {group_data_file}")

# Función para generar nombres de método basados en columnas y funciones de agregación
def generate_method_name(columns, agg_dict):
    column_str = "_".join(columns)
    agg_str = "_".join([f"{col}_{func}" for col, func in agg_dict.items()])
    return f"df_{column_str}_{agg_str}"

# Función para generar el contenido del método de agrupamiento
def generate_group_method_content(columns, agg_dict, options):
    method_name = generate_method_name(columns, agg_dict)
    
    method_content = f"    def {method_name}(self):\n"
    method_content += f"        if all(col in self.dataframe.columns for col in {columns}):\n"
    method_content += f"            result = self.dataframe.groupby({columns}).agg({agg_dict})\n"
    
    # Verificar si se debe hacer reset_index
    if 'reset_index' in options and options['reset_index']:
        method_content += f"            return result.reset_index()\n"
    else:
        method_content += f"            return result\n"
    
    method_content += f"        else:\n"
    method_content += f"            raise ValueError('Las columnas especificadas no existen en el dataframe')\n\n"

    return method_content




# # Llamar a la función si el script se ejecuta directamente
# if __name__ == "__main__":
#     my_models_path = os.path.join(base_path, 'my_models/concrete_models')
#     group_params_list = [
#         (['Escuela_ID', 'CURSO_NORMALIZADO'], {'Alumno_ID': 'count'}),
#         (['Profesor_ID'], {'Nota': 'mean'})
#     ]
#     add_group_methods_to_class(my_models_path, 'Group', group_params_list)
