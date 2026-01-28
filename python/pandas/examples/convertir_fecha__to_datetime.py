"""
Objetivo: convertir columna a tipo datetime
Referencia: to_datetime
Tipo: funcion
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Convertir columna fecha a datetime
df["fecha"] = pd.to_datetime(df["fecha"])

print(df.dtypes)
print()
print(df[["fecha", "producto"]].head())

"""output
fecha             datetime64[ns]
producto_id               int64
producto                 object
categoria                object
precio                 float64
stock                   int64
descuento              float64
cliente_id              object
dtype: object

       fecha           producto
0 2024-01-01      Laptop ASUS
1 2024-01-02  Mouse Logitech
2 2024-01-03 Teclado Mecánico
3 2024-01-04    Monitor LG 24
4 2024-01-05 Escritorio Gamer
"""