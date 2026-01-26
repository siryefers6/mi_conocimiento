"""
Objetivo: analizar la frecuencia de valores en una columna categórica
Referencia: value_counts
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: frecuencia por canal
frecuencia = df["canal"].value_counts()

# resultado
print(frecuencia)

"""output
canal
online    6
tienda    4
Name: count, dtype: int64
"""
