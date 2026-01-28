"""
Objetivo: usar operaciones vectorizadas con NumPy
Referencia: numpy
Tipo: libreria
Nivel: avanzado
Dataset: ventas.csv
"""

import pandas as pd
import numpy as np

df = pd.read_csv("datasets/ventas.csv")

# Crear categoría de precio con np.where
df["rango_precio"] = np.where(df["precio"] > 500, "Alto", "Bajo")

print(df[["producto", "precio", "rango_precio"]].head())

"""output
            producto    precio rango_precio
0       Laptop ASIS   1200.00        Alto
1     Mouse Logitech     25.99        Bajo
2    Teclado Mecánico     85.50        Bajo
3       Monitor LG 24    300.00        Bajo
4    Escritorio Gamer    450.00        Bajo
"""