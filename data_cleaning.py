import pandas as pd

data = pd.read_csv('survey_results_schema.csv')

print("Columnas del archivo CSV:")
print(data.columns)

data['qid'] = data['qid'].astype(str)

data['question'] = data['question'].str.replace('\n', ' ').str.strip()

data['force_resp'] = data['force_resp'].astype(bool)

print("\nVerificando valores nulos:")
print(data.isnull().sum())

data.to_csv('archivo_limpio.csv', index=False)
print("\nArchivo limpio guardado como 'archivo_limpio.csv'.")
