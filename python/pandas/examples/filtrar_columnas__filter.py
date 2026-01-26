"""
Objetivo: filtrar columnas por nombre
Referencia: filter
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# filtrar columnas que contienen la palabra 'prod'
columnas = df.filter(like="prod")

# resultado
print(columnas)

"""output
   producto_id    producto
0          101      Laptop
1          102       Mouse
2          103     Teclado
3          104       Silla
4          105  Escritorio
5          106     Monitor
6          107   Impresora
7          108  Cable HDMI
8          109      Webcam
9          110      Router
"""
