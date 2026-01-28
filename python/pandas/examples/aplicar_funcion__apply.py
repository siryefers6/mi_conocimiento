"""
Objetivo: aplicar una función a columnas o filas
Referencia: apply
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Aplicar función para calcular margen de descuento
df["precio_final"] = df.apply(lambda row: row["precio"] * (1 - row["descuento"]), axis=1)

print(df[["producto", "precio", "descuento", "precio_final"]].head())

"""output
            producto    precio  descuento    precio_final
0       Laptop ASUS   1200.00       0.10    1080.000000
1     Mouse Logitech     25.99       0.00      25.990000
2    Teclado Mecánico     85.50       0.05      81.225000
3       Monitor LG 24    300.00       0.15     255.000000
4    Escritorio Gamer    450.00       0.20     360.000000
"""