"""
Objetivo: Detectar valores nulos en el DataFrame
Referencia: isnull
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos con valores faltantes
df = pd.read_csv('../datasets/frutas.csv')

# Detectar nulos
resultado = df.isnull()
print(resultado)

"""output
   id  producto  cantidad  precio   fecha
0  False     False     False   False  False
1  False     False     False   False  False
2  False     False     False    True  False
3  False     False     False   False  False
4  False     False      True   False  False
5  False     False     False   False  False
6  False     False     False   False  False
7  False     False      True   False  False
8  False     False     False   False  False
9  False     False     False   False  False
"""
