from abc import ABC, abstractmethod
import pandas as pd
import json
import utils as u

"""
Esta clase va a dirigir el reporte.
Va a tener la habilidad de poder ir armando el .json.
Va a recibir una cantidad no definida de dataframes
para usarla se debe crear una clase concreta de la siguiente forma:

import json
import pandas as pd

class ConcreteReport(AbstractReport):
    def __init__(self, *dataframes: pd.DataFrame):
        super().__init__(*dataframes)

    def report(self, output_path: str):
        report_data = {}
        for i, df in enumerate(self.dataframes):
            report_data[f"DataFrame_{i+1}"] = df.to_dict(orient='records')

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, ensure_ascii=False, indent=4)
        print(f"Reporte generado exitosamente en {output_path}")

import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})

report = ConcreteReport(df1, df2)
report.report('output_report.json')
"""

class AbstractReport(ABC):

    def __init__(self, output_path, *args ):
        self.output_path = output_path
        self.additional_params = args 
        self.report_data = None

    @abstractmethod
    def do_report(self):
        pass
    
    def save_report(self):
        u.save_json(self.report_data, self.output_path)

    def view_report(self):
        print(self.additional_params[0][0])
        print(self.additional_params[0][1])
        print(self.additional_params[0][2])
        print(self.report_data)