"""
Objetivo: contar valores no nulos por columna
Referencia: count
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: conteo de valores no nulos
conteo = df.count()

# resultado
print(conteo)

"""output
fecha          10
producto_id    10
producto       10
categoria      10
precio         10
stock           9
ventas          9
canal          10
descuento       8
cliente_id      9
dtype: int64
"""
