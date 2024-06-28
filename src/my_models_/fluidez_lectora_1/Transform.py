from src.abstract_model.AbstractTransform import AbstractTransform
import pandas as pd

class Transform(AbstractTransform):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def transform_data(self):
        pass

