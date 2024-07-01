from src.abstract_model.AbstractReport import AbstractReport
import pandas as pd

class Report(AbstractReport):
    def __init__(self, output_path, *args):
        super().__init__(output_path, args)

    def do_report(self, *args, **kwargs):
        pass

