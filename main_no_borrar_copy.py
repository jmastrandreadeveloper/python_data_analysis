import os
import sys
from src.data_loading import DataLoader

import src.utils as u

# obligatorio para poder acceder a todas las funcionalidades de las librerias para el proyecto y todo lo demas
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

def main():

    u.create_folder_tree('_nominal_para_fluidez_Lectora_1_')
    u.create_folder_tree('_análisis_fluidez_Lectora_1_')

    loader = DataLoader('Nominal.csv')
    dfnom = loader.load_csv()   

    loader = DataLoader('Fluidez Lectora 1.csv')
    df_FluidezLectora_1 = loader.load_csv()    
    
    from src.my_models_._nominal_para_fluidez_Lectora_1_ import Main as mNom
    nom = mNom(dfnom)
    
    from src.my_models_._análisis_fluidez_Lectora_1_ import Main as mFL1
    fl1 = mFL1(df_FluidezLectora_1)

    return

if __name__ == "__main__":
    main()