from src.data_loading import DataLoader
from src.preprocessing import clean_data, transform_data, validate_data
from src.analysis import Analyzer
from src.utils import ensure_dir, save_dataframe_to_csv, save_image
from PIL import Image  # Asegúrate de que tienes Pillow instalado


def main():
    print("Asegurando directorios necesarios...")
    ensure_dir('data/processed')
    ensure_dir('data/processed/images')
    ensure_dir('data/processed/otrodir')

    # Carga de datos
    loader = DataLoader('Nominal.csv')
    df_nominal = loader.load_csv()

    loader = DataLoader('Fluidez Lectora 1.csv')
    df_FL_1 = loader.load_csv()

    

    print("Preprocesando datos...")
    # Preprocesamiento de datos
    df_FL_1 = clean_data(df_FL_1)
    df_FL_1 = transform_data(df_FL_1)
    
    # Validar los datos nominales
    is_valid, df_nominal_validated = validate_data(df_nominal)
    if not is_valid:
        print("La validación de los datos nominales ha fallado.")
        return

    print("Guardando datos procesados...")
    # Guardar datos procesados
    save_dataframe_to_csv(df_FL_1, 'data/processed/transformed/transformed_dataset.csv')
    save_dataframe_to_csv(df_nominal_validated, 'data/processed/transformed/df_nominal_validated.csv')

    # print("Procesando y guardando imagen...")
    # # Procesamiento y guardado de una imagen (ejemplo)
    # image = Image.open('data/raw/sample_image.jpg')
    # processed_image = image.convert('L')  # Ejemplo de procesamiento simple
    # save_image(processed_image, 'data/processed/images/processed_image.jpg')

    # print("Analizando datos...")
    # # Análisis de datos
    # analyzer = Analyzer(data)
    # analyzer.plot_histogram('some_column')
    # stats = analyzer.calculate_statistics()
    # print(stats)

if __name__ == "__main__":
    main()