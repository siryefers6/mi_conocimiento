"""
Objetivo: Sumar valores por grupo
Referencia: groupby().sum
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Sumar salarios por departamento
resultado = df.groupby('departamento')['salario'].sum()
print(resultado)

"""output
departamento
Dirección          95000
Finanzas          157000
IT                187000
Recursos Humanos   48000
Ventas            147000
Name: salario, dtype: int64
"""
