"""
Objetivo: seleccionar una columna del DataFrame
Referencia: []
Tipo: sintaxis
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

producto = df["producto"]

print(producto.head())

"""output
0         Laptop ASUS
1      Mouse Logitech
2    Teclado Mecánico
3       Monitor LG 24
4    Escritorio Gamer
Name: producto, dtype: object
"""