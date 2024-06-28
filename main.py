import os
import sys

from src.data_loading import DataLoader
from src.analysis import Analyzer
from src.reports import ReporteFluidezLectora_1_PorEscuela

def main():
    #### generador de clases concretas ##################################################################
    # Agregar el directorio raíz del proyecto al sys.path
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
    from generator import generate_concrete_classes
    # Directorio de salida para las clases concretas
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src/my_models_')
    # Generar clases concretas
    # group_params_list = [
    #     (['Escuela_ID', 'CURSO_NORMALIZADO'], {'Alumno_ID': 'count'}),
    #     (['Escuela_ID','CURSO_NORMALIZADO','División'], {'Alumno_ID': 'count'})
    # ]
    generate_concrete_classes(output_dir , 'fluidez_lectora_1') #, group_params_list )
    #####################################################################################################

    loader = DataLoader('Fluidez Lectora 1.csv')
    df_FluidezLectora_1 = loader.load_csv()

    # test concretas
    # para testear las clases que se generan
    from src.my_models_.fluidez_lectora_1.Preprocessor import Preprocessor
    from src.my_models_.fluidez_lectora_1.Group import Group
    from src.my_models_.fluidez_lectora_1.Transform import Transform
    fl_1_concrete = Preprocessor(df_FluidezLectora_1)
    fl_1_concrete.método_concreto()

    #### generador de clases concretas ##################################################################
    from generator_groups import generate_group_data_class
    base_path = os.path.dirname(os.path.abspath(__file__))    
    #my_models_path = os.path.join(base_path, 'src/my_models_/fluidez_lectora_1')
    group_params_list = [
        (['Escuela_ID', 'CURSO_NORMALIZADO'], {'Alumno_ID': 'count'},{'reset_index': True}),
        (['Escuela_ID','CURSO_NORMALIZADO','División'], {'Alumno_ID': 'count'},{'reset_index': False}),
        (['Nivel','CURSO_NORMALIZADO','División'], {'Alumno_ID': 'count'},{'reset_index': True}),
    ]
    generate_group_data_class(group_params_list , 'src/my_models_/fluidez_lectora_1')
    #####################################################################################################

    fl_1_group = Group(df_FluidezLectora_1)
    fl_1_group.group_data()

    fl_1_transform = Transform(df_FluidezLectora_1)
    print(fl_1_transform.mergue_data(fl_1_group.d1 , fl_1_group.d2 , 'Alumno_ID' , 'left' ))

    


    print('..fin..')


if __name__ == "__main__":
    main()