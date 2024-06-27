import pandas as pd
from src.models2.bgrouping.abstract_group import AbstractGroup

class Group(AbstractGroup):  
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)
        
    def group_data(self):
        return 'group'