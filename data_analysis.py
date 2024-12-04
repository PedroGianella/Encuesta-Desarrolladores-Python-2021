import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('archivo_limpio.csv')

print("Columnas del archivo limpio:")
print(data.columns)

if 'salary' in data.columns and 'company' in data.columns:
    salario_empresa = data.groupby('company')['salary'].mean().sort_values(ascending=False)
    print("\nSalarios promedio por empresa:")
    print(salario_empresa)
    salario_empresa.plot(kind='bar', title='Salarios promedio por empresa')
    plt.show()

if 'RemoteWork' in data.columns:
    trabajo_distancia = data['RemoteWork'].value_counts()
    print("\nImportancia del trabajo a distancia:")
    print(trabajo_distancia)
    trabajo_distancia.plot(kind='pie', title='Trabajo a distancia')
    plt.show()

if 'experience' in data.columns and 'salary' in data.columns:
    experiencia_salario = data.groupby('experience')['salary'].mean()
    print("\nSalario promedio según experiencia:")
    print(experiencia_salario)
    experiencia_salario.plot(kind='line', title='Relación entre experiencia y salario')
    plt.show()

if 'LearnCode' in data.columns:
    metodos_aprendizaje = data['LearnCode'].value_counts()
    print("\nMétodos populares para aprender a programar:")
    print(metodos_aprendizaje)
    metodos_aprendizaje.plot(kind='bar', title='Métodos populares para aprender a programar')
    plt.show()

if 'EdLevel' in data.columns and 'job_status' in data.columns:
    empleo_master = data.groupby('EdLevel')['job_status'].mean()
    print("\nProbabilidad de conseguir empleo según nivel educativo:")
    print(empleo_master)
    empleo_master.plot(kind='bar', title='Probabilidad de conseguir empleo según nivel educativo')
    plt.show()
