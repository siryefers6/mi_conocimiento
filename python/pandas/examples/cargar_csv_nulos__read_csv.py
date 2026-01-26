"""
Objetivo: cargar un CSV definiendo valores personalizados como nulos
Referencia: read_csv
Tipo: funcion
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

# definición de valores que deben considerarse nulos
valores_nulos = ["", "NA", "N/A", "null"]

# carga de datos
df = pd.read_csv(
    "datasets/ventas.csv",
    na_values=valores_nulos
)

# resultado
print(df.isna().sum())

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
