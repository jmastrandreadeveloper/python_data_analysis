import os
import sys


from src.data_loading import DataLoader
from src.preprocessing import clean_data, transform_data_fluidez_lectora, validate_data
from src.analysis import Analyzer
from src.reports import ReporteFluidezLectora_1_PorEscuela
from src.utils import ensure_dir, save_dataframe_to_csv, obtener_datos_de_columna , save_image
from PIL import Image  # Asegúrate de que tienes Pillow instalado
from src.NoBorrar_models.specific_dataframe import SpecificDataFrame
from src.NoBorrar_models.specific_dataframe_fluidez_lectora import SpecificDataFrameFluidezLectora

from src.my_models.fluidez_lectora_1.a_prepocessor import Preprocessor
from src.my_models.fluidez_lectora_1.b_agg import Agg
from src.my_models.fluidez_lectora_1.b_group import Group
from src.my_models.fluidez_lectora_1.c_filter import Filter



def main():
    #### generador de clases concretas ##################################################################
    # Agregar el directorio raíz del proyecto al sys.path
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
    from generator import generate_concrete_classes
    # Directorio de salida para las clases concretas
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src/my_models_')
    # Generar clases concretas
    generate_concrete_classes(output_dir , 'fluidez_lectora_1')
    ######################################################################################################





    print("Asegurando directorios necesarios...")
    ensure_dir('data/processed')
    ensure_dir('data/processed/images')
    ensure_dir('data/processed/otrodir')

    # Carga de datos
    loader = DataLoader('Nominal.csv')
    dfnom = loader.load_csv()

    loader = DataLoader('Fluidez Lectora 1.csv')
    df_FluidezLectora_1 = loader.load_csv()


    

    # test concretas
    # para testear las clases que se generan
    from src.my_models_.fluidez_lectora_1.Preprocessor import Preprocessor    
    fl_1_concrete = Preprocessor(df_FluidezLectora_1)
    fl_1_concrete.método_concreto()
    


    ############################### experimento ##################################
    # Preproceso de fl 1
    fl_1_processed = Preprocessor(df_FluidezLectora_1)
    c = fl_1_processed.cleaning_data()
    t = fl_1_processed.transform_data()
    v = fl_1_processed.validate_data()
    f = fl_1_processed.filter_data()
    print(c , ' ' , t , ' ' , v , ' ' , f , ' ' ,)
    # Agrupado de fl 1
    fl_1_groupped = Group(fl_1_processed)
    g = fl_1_groupped.group_data()
    print(g)
    # Agregado
    fl_1_agregado = Agg(fl_1_groupped)
    a = fl_1_agregado.agg_data()
    print(a)
    # Filtrado
    fl_1_filtrado = Filter(fl_1_agregado)
    fi = fl_1_filtrado.filter_data()
    print(fi)
    ############################# fin experimento ################################

    print("Preprocesando datos...")
    # Preprocesamiento de datos
    # esto hay que reconsiderar si se queda acá 
    # o lo muevo dentro de la clase específica 
    df_FluidezLectora_1 = clean_data(df_FluidezLectora_1)    
    
    # esta función debería traerme todos los agrupamientos que yo necesite
    df_FluidezLectora_1 = transform_data_fluidez_lectora(df_FluidezLectora_1)
    # Crear instancia de la clase específica de fl 
    obj_df_1 = SpecificDataFrameFluidezLectora(df_FluidezLectora_1)
    # grabo los distintos dataframes
    save_dataframe_to_csv(obj_df_1.df_Desempeño_por_Escuela, 'data/processed/transformed/df_Desempeño_por_Escuela.csv')
    save_dataframe_to_csv(obj_df_1.df_Desempeño_por_Escuela_CURSO_NORMALIZADO, 'data/processed/transformed/df_Desempeño_por_Escuela_CURSO_NORMALIZADO.csv')
    save_dataframe_to_csv(obj_df_1.df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division, 'data/processed/transformed/df_Desempeño_por_Escuela_CURSO_NORMALIZADO_Division.csv')
    save_dataframe_to_csv(obj_df_1.df_Desempeño_por_Nivel_CURSO_NORMALIZADO, 'data/processed/transformed/df_Desempeño_por_Nivel_CURSO_NORMALIZADO.csv')
    save_dataframe_to_csv(obj_df_1.df_Desempeño_por_Supervisión_CURSO_NORMALIZADO, 'data/processed/transformed/df_Desempeño_por_Supervisión_CURSO_NORMALIZADO.csv')


    
    # Validar los datos nominales
    is_valid, dfnom_validated = validate_data(dfnom)
    if not is_valid:
        print("La validación de los datos nominales ha fallado.")
        return

    print("Guardando datos procesados...")
    # Guardar datos procesados
    save_dataframe_to_csv(dfnom_validated, 'data/processed/transformed/dfnom_validated_transformed_dataset.csv')
    save_dataframe_to_csv(dfnom_validated, 'data/processed/transformed/dfnom_validated.csv') # este se usa para sacar los datos de las escuelas..

    #save_dataframe_to_csv(dFsss_, 'data/processed/transformed/df_FluidezLectora_1.csv') # este se usa para sacar los datos de las escuelas..

    # creo los reportes por escuela que serán guiados mediante 
    # la lista de todas las escuelas a analizar
    # además debería poder pasarle todos los datos ya agrupados para que los filtre por escuela
    # esos datos deben ser agrupados en la llamada a la función transform_data la cual
    # va a devolver todos los dataframes agrupados que necesitemos para ser filtrados por escuela
    reportePorEscuela = ReporteFluidezLectora_1_PorEscuela(dfnom_validated , df_FluidezLectora_1)
    # acá llamaría a un método de analyzer para que 
    # haga el bucle principal para tener los informes
    Escuelas_IDs = reportePorEscuela.hacer_reporte_por_lista_de_escuelas()

    # imprimo los id de las escuelas a analizar..
    # luego comentar estas lineas..
    # for i in Escuelas_IDs:
    #     print(i)

    # print("Procesando y guardando imagen...")
    # # Procesamiento y guardado de una imagen (ejemplo)
    # image = Image.open('data/raw/sample_image.jpg')
    # processed_image = image.convert('L')  # Ejemplo de procesamiento simple
    # save_image(processed_image, 'data/processed/images/processed_image.jpg')

    print("Analizando datos...")
    # Análisis de datos
    # voy a usar el que está validado de ejemplo..pero solo a modo de ejemplo
    # loader = DataLoader('transformed_dataset.csv')
    # transformed_dataset = loader.load_csv()
    # analyzer = Analyzer(transformed_dataset)
    # analyzer.plot_histogram('new_column')
    # stats = analyzer.calculate_statistics()
    # print(stats)

if __name__ == "__main__":
    main()