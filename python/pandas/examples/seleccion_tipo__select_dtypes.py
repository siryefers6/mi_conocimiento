"""
Objetivo: Seleccionar columnas por tipo de dato
Referencia: select_dtypes
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Seleccionar solo columnas numéricas
resultado = df.select_dtypes(include=['int64'])
print(resultado.head())

"""output
   id  edad  salario
0   1    28    45000
1   2    34    65000
2   3    45    75000
3   4    29    62000
4   5    51    95000
"""
