"""
Objetivo: Calcular promedio de valores por grupo
Referencia: groupby().mean
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Promedio de salarios por departamento
resultado = df.groupby('departamento')['salario'].mean()
print(resultado)

"""output
departamento
Dirección          95000.000000
Finanzas           78500.000000
IT                 62333.333333
Recursos Humanos   48000.000000
Ventas             49000.000000
Name: salario, dtype: float64
"""
