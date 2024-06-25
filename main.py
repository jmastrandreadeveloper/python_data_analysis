from src.data_loading import DataLoader
from src.preprocessing import clean_data, transform_data, validate_data
from src.analysis import Analyzer
from src.reports import ReporteFluidezLectora_1_PorEscuela
from src.utils import ensure_dir, save_dataframe_to_csv, obtener_datos_de_columna , save_image
from PIL import Image  # Asegúrate de que tienes Pillow instalado
from src.models.specific_dataframe import SpecificDataFrame


def main():
    print("Asegurando directorios necesarios...")
    ensure_dir('data/processed')
    ensure_dir('data/processed/images')
    ensure_dir('data/processed/otrodir')

    # Carga de datos
    loader = DataLoader('Nominal.csv')
    dfnom = loader.load_csv()

    loader = DataLoader('Fluidez Lectora 1.csv')
    df_FluidezLectora_1 = loader.load_csv()    

    print("Preprocesando datos...")
    # Preprocesamiento de datos    
    df_FluidezLectora_1 = clean_data(df_FluidezLectora_1)
    # Crear instancia de la clase específica
    specific_df = SpecificDataFrame(df_FluidezLectora_1)
    specific_df.imprimir()
    # en la llamada de abajo se hacen todos los agrupamientos necesarios
    # esta función debería traerme todos los agrupamientos que yo necesite
    dFsss_ = transform_data(df_FluidezLectora_1)
    
    # Validar los datos nominales
    is_valid, dfnom_validated = validate_data(dfnom)
    if not is_valid:
        print("La validación de los datos nominales ha fallado.")
        return

    print("Guardando datos procesados...")
    # Guardar datos procesados
    save_dataframe_to_csv(dfnom_validated, 'data/processed/transformed/dfnom_validated_transformed_dataset.csv')
    save_dataframe_to_csv(dfnom_validated, 'data/processed/transformed/dfnom_validated.csv') # este se usa para sacar los datos de las escuelas..

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
    for i in Escuelas_IDs:
        print(i)

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