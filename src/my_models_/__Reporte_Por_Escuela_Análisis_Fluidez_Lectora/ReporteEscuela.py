#from src.my_models_._abstract_model_.AbstractReport import AbstractReport
from src.my_models_.__Nominal_para_fluidez_Lectora_1_.Report import Report as rNom
from src.my_models_.__Análisis_Fluidez_Lectora_1_.Report import Report as rAFL
import pandas as pd
import src.my_models_.__Análisis_Fluidez_Lectora_1_.Filtros.filtro1 as f
from dataclasses import dataclass

@dataclass #(frozen=True)
class ReporteEscuela : #(AbstractReport):

    reporteNominal  :   rNom
    reporteFluidez  :   rAFL    

    def do_report(self):
        self.do_report_escuela()
    
    def do_report_escuela(self, *args, **kwargs): 
        print('reporte por escuela de fluidez lectora')        
        f.filtro()
        print('..parámetros de nominal.. ' , self.reporteNominal.parametro_Nominal)
        print('..parámetros de fluidez.. ' , self.reporteFluidez.parametro_Fluidez)
        #self.view_report()
        pass

    def a(self):
        print('esta')