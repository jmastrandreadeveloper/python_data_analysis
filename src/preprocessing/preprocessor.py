class Preprocessor:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        # Implementa limpieza de datos
        return self.data.dropna()

    def transform_data(self):
        # Implementa transformaciones necesarias
        return self.data
