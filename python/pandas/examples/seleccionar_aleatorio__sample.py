"""
Objetivo: seleccionar filas aleatorias del DataFrame
Referencia: sample
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Seleccionar 3 filas aleatorias
resultado = df.sample(n=3, random_state=42)

print(resultado[["producto", "precio", "stock"]])

"""output
            producto    precio  stock
13 Escritorio Gamer   450.00      2
7      Cable HDMI 2m    15.00    100
4      Escritorio Gamer   450.00      3
"""