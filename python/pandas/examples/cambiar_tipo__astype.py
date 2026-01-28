"""
Objetivo: cambiar el tipo de datos de una columna
Referencia: astype
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Convertir descuento a entero (para porcentaje)
df["descuento_porcentaje"] = (df["descuento"] * 100).astype("int")

print(df[["producto", "descuento", "descuento_porcentaje"]].head())

"""output
            producto  descuento  descuento_porcentaje
0       Laptop ASUS       0.10                    10
1     Mouse Logitech       0.00                     0
2    Teclado Mecánico       0.05                     5
3       Monitor LG 24       0.15                    15
4    Escritorio Gamer       0.20                    20
"""