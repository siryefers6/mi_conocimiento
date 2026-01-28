"""
Objetivo: ordenar DataFrame por una o más columnas
Referencia: sort_values
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Ordenar por precio descendente
resultado = df.sort_values("precio", ascending=False)

print(resultado[["producto", "precio", "categoria"]].head())

"""output
          producto    precio      categoria
0      Laptop ASUS   1200.00   Electrónica
10     Laptop ASUS   1200.00   Electrónica
11     Laptop ASUS   1200.00   Electrónica
5   Monitor Dell 27   500.00   Electrónica
4  Escritorio Gamer   450.00      Muebles
"""