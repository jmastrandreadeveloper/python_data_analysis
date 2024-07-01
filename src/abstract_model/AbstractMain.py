from abc import ABC, abstractmethod
import pandas as pd
from src.abstract_model.AbstractGroupAggregation import AbstractGroupAggregation
from src.abstract_model.AbstractPreprocessor import AbstractPreprocessor
from src.abstract_model.AbstractTransform import AbstractTransform
from src.abstract_model.AbstractReport import AbstractReport

"""
AbstractMain: Esta clase hereda de las tres clases abstractas 
(AbstractGroupAggregation, AbstractPreprocessor, AbstractTransform) 
y define un método abstracto run_all que deberá ser implementado por la clase concreta.

Main: Esta clase concreta implementa todos los métodos abstractos heredados 
y define el método run_all que puede utilizar todas las funcionalidades disponibles en las clases base.
Esta estructura permite que la clase Main acceda a todas las funcionalidades de agrupación, 
preprocesamiento y transformación de datos definidas en las clases abstractas. 
Además, la clase Main puede ser extendida o personalizada según las necesidades específicas del proyecto.
"""
class AbstractMain:#(AbstractGroupAggregation, AbstractPreprocessor, AbstractTransform , AbstractReport):

    def __init__(self, dataframe: pd.DataFrame):
        # AbstractGroupAggregation.__init__(self, dataframe)
        # AbstractPreprocessor.__init__(self, dataframe)
        # AbstractTransform.__init__(self, dataframe)
        # AbstractReport.__init__(self, dataframe)
        self.dataframe = dataframe

    @abstractmethod
    def run_all(self):
        pass
