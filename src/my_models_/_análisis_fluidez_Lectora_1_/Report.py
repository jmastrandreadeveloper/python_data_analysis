from src.abstract_model.AbstractReport import AbstractReport
import pandas as pd

class Report(AbstractReport):
    def __init__(self, output_path, *args):
        super().__init__(output_path, args)

    def do_report(self, *args, **kwargs):
        pass

    def func(self):
        dic = {
            'a' : 10,
            'b' : 20
        }
        print('acá va el reporte' ,  dic)

