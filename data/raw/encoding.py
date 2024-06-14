# https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/
# https://sparrow.dev/pandas-rename-column/

# importing the pandas library
import pandas as pd

original = 'Fluidez Lectora 1.csv'
salida = 'Fluidez Lectora 1_.csv'


sep_            = ';'
encoding_       = "UTF-8"
lineterminator_ = '\n'

# reading the csv file
df = pd.read_csv(original ,  sep = sep_ , encoding = encoding_ , lineterminator= lineterminator_)
#df = pd.read_csv(original ,  sep_ , encoding_ ,  lineterminator_)
#df = pd.read_csv(original ,  header=0 , delimiter=";")

  
# writing into the file
df.to_csv(salida, index=False, sep=';', encoding="UTF-8", line_terminator='\n')
  
print(df)