from src.my_models_._abstract_model_.AbstractReport import AbstractReport
import pandas as pd
import src.my_models_.__Análisis_Fluidez_Lectora_1_.Filtros.filtro1 as f

class Report(AbstractReport):
    def __init__(self, output_path, *args):
        super().__init__(output_path, args)
        self.parametro_Fluidez = 20

    def do_report(self, *args, **kwargs):
        f.filtro()
        pass

