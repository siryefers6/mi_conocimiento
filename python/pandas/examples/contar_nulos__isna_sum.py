"""
Objetivo: contar valores nulos por columna
Referencia: isna().sum()
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# conteo de valores nulos por columna
conteo_nulos = df.isna().sum()

# resultado
print(conteo_nulos)

"""output
fecha          0
producto_id    0
producto       0
categoria      0
precio         0
stock          1
ventas         1
canal          0
descuento      2
cliente_id     1
dtype: int64
"""
