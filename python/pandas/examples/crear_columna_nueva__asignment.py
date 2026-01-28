"""
Objetivo: crear una columna nueva en el DataFrame
Referencia: asignment
Tipo: sintaxis
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Crear columna de precio total
df["total"] = df["precio"] * df["stock"]

print(df[["producto", "precio", "stock", "total"]].head())

"""output
            producto    precio  stock      total
0       Laptop ASUS   1200.00     10  12000.00
1     Mouse Logitech     25.99     50   1299.50
2    Teclado Mecánico     85.50     30   2565.00
3       Monitor LG 24    300.00      5   1500.00
4    Escritorio Gamer    450.00      3   1350.00
"""