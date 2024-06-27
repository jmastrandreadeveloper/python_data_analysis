from AbstractGroup import AbstractGroup
import pandas as pd

class ConcreteAbstractGroup(AbstractGroup):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def group_data(self):
        pass

