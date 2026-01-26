"""
Objetivo: seleccionar múltiples columnas de un DataFrame
Referencia: []
Tipo: sintaxis
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# selección de múltiples columnas
columnas = df[["producto", "precio", "ventas"]]

# resultado
print(columnas)

"""output
     producto   precio  ventas
0      Laptop     1200     5.0
1       Mouse       25    20.0
2     Teclado       45    15.0
3       Silla      300     2.0
4  Escritorio      450     1.0
5     Monitor  500 USD     4.0
6   Impresora      250     0.0
7  Cable HDMI       15    60.0
8      Webcam       85     NaN
9      Router      120     7.0
"""
