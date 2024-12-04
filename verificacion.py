import pandas as pd

# Cargar el archivo CSV (ajusta el nombre del archivo según corresponda)
data = pd.read_csv('survey_results_schema.csv')

# Imprimir las columnas del archivo
print("Columnas del archivo CSV:")
print(data.columns)
