from src.abstract_model.AbstractGroup import AbstractGroup
from src.my_models_.fluidez_lectora_1.GroupData import GroupData
import pandas as pd

class Group(AbstractGroup):
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(dataframe)

    def group_data(self):
        gd = GroupData(self.dataframe)
        self.d1 = gd.df_Escuela_ID_CURSO_NORMALIZADO_Alumno_ID_count()
        self.d2 = gd.df_Escuela_ID_CURSO_NORMALIZADO_División_Alumno_ID_count()
        
        return self.d1 , self.d2

