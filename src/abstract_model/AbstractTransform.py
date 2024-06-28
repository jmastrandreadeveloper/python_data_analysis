from abc import ABC, abstractmethod
import pandas as pd

class AbstractTransform(ABC):
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe

    @abstractmethod
    def transform_data(self):
        pass

    def mergue_data(self,df_left , df_right , mergeOnColumn , how_) -> pd.DataFrame:
        return pd.merge(df_left, df_right, how=how_, on=mergeOnColumn)