"""
Objetivo: Convertir string a minúsculas
Referencia: .str.lower
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Convertir a minúsculas
resultado = df['nombre'].str.lower()
print(resultado.head())

"""output
0      juan
1     maría
2    carlos
3       ana
4     pedro
Name: nombre, dtype: object
"""
