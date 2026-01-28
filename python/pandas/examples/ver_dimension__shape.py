"""
Objetivo: obtener dimensiones del DataFrame
Referencia: shape
Tipo: atributo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

filas, columnas = df.shape

print(f"Filas: {filas}")
print(f"Columnas: {columnas}")

"""output
Filas: 20
Columnas: 8
"""