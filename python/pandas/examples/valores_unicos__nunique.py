"""
Objetivo: contar valores únicos por columna
Referencia: nunique
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: cantidad de valores únicos
unicos = df.nunique()

# resultado
print(unicos)

"""output
fecha          10
producto_id    10
producto       10
categoria       3
precio         10
stock           8
ventas          8
canal           2
descuento       5
cliente_id      9
dtype: int64
"""
