from src.abstract_model.AbstractTransform import AbstractTransform
import pandas as pd

class Transform(AbstractTransform):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def apply(self, *args, **kwargs):
        pass

    def map(self, *args, **kwargs):
        pass

    def applymap(self, *args, **kwargs):
        pass

    def astype(self, *args, **kwargs):
        pass

    def melt(self, *args, **kwargs):
        pass

    def resample(self, *args, **kwargs):
        pass

    def rolling(self, *args, **kwargs):
        pass

