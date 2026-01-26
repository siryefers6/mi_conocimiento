"""
Objetivo: conocer la cantidad de filas y columnas de un DataFrame
Referencia: shape
Tipo: atributo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: obtener dimensiones
dimensiones = df.shape

# resultado
print(dimensiones)

"""output
(10, 10)
"""
