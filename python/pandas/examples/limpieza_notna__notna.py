"""
Objetivo: Detectar valores no nulos
Referencia: notna
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos con valores faltantes
df = pd.read_csv('../datasets/frutas.csv')

# Detectar valores NO nulos
resultado = df.notna()
print(resultado)

"""output
       id  producto  cantidad  precio   fecha
0   True      True      True    True   True
1   True      True      True    True   True
2   True      True      True   False   True
3   True      True      True    True   True
4   True      True     False    True   True
5   True      True      True    True   True
6   True      True      True    True   True
7   True      True     False    True   True
8   True      True      True    True   True
9   True      True      True    True   True
"""
