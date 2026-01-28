"""
Objetivo: filtrar columnas por patrón de nombre
Referencia: filter
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Filtrar columnas que contengan "o"
resultado = df.filter(like="o")

print(resultado.head())

"""output
  producto categoria  stock descuento
0 Laptop ASUS   Electrónica     10      0.10
1 Mouse Logitech    Accesorios     50      0.00
2 Teclado Mecánico   Accesorios     30      0.05
3 Monitor LG 24   Electrónica      5      0.15
4 Escritorio Gamer      Muebles      3      0.20
"""