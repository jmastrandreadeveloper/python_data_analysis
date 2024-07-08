from src.my_models_._abstract_model_.AbstractReport import AbstractReport
import pandas as pd

class Report(AbstractReport):
    def __init__(self, output_path, *args):
        super().__init__(output_path, args)
        # self.listaEscuelas_IDs = args[0]
        # self.dataframe = args[1]
        # self.parametro_Nominal = 10

    def do_report(self, *args, **kwargs):
        #print(self.listaEscuelas_IDs)
        pass

