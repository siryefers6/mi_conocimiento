"""
Objetivo: detectar valores nulos en un DataFrame
Referencia: isna
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# detección de valores nulos
nulos = df.isna()

# resultado
print(nulos)

"""output
   fecha  producto_id  producto  categoria  precio  stock  ventas  canal  descuento  cliente_id
0  False        False     False      False   False  False   False  False      False       False
1  False        False     False      False   False  False   False  False       True       False
2  False        False     False      False   False   True   False  False      False       False
3  False        False     False      False   False  False   False  False      False        True
4  False        False     False      False   False  False   False  False      False       False
5  False        False     False      False   False  False   False  False      False       False
6  False        False     False      False   False  False   False  False      False       False
7  False        False     False      False   False  False   False  False       True       False
8  False        False     False      False   False  False    True  False      False       False
9  False        False     False      False   False  False   False  False      False       False
"""
