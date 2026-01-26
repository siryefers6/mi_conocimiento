"""
Objetivo: cambiar el tipo de datos de columnas
Referencia: astype
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# normalización previa
df["precio"] = df["precio"].replace({"500 USD": 500})
df["precio"] = pd.to_numeric(df["precio"], errors="coerce")

# cambio de tipo
df["producto_id"] = df["producto_id"].astype(int)
df["precio"] = df["precio"].astype(float)
df["ventas"] = df["ventas"].fillna(0).astype(int)

# resultado
print(df.dtypes)

"""output
fecha           object
producto_id      int64
producto        object
categoria       object
precio         float64
stock          float64
ventas           int64
canal           object
descuento      float64
cliente_id      object
dtype: object
"""
