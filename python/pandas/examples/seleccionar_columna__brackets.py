"""
Objetivo: seleccionar una columna de un DataFrame
Referencia: []
Tipo: sintaxis
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# selección de una columna
columna = df["producto"]

# resultado
print(columna)

"""output
0        Laptop
1         Mouse
2       Teclado
3         Silla
4    Escritorio
5       Monitor
6     Impresora
7    Cable HDMI
8        Webcam
9        Router
Name: producto, dtype: object
"""
