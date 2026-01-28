"""
Objetivo: contar ocurrencias de valores en una columna
Referencia: value_counts
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Contar productos vendidos
resultado = df["producto"].value_counts()

print(resultado)

"""output
Laptop ASUS           3
Mouse Logitech        2
Monitor LG 24         2
Monitor Dell 27       2
Escritorio Gamer      2
Cable HDMI 2m         2
Auriculares Sony      1
Teclado Mecánico      1
Webcam Logitech       1
Micrófono USB         1
Name: producto, dtype: int64
"""