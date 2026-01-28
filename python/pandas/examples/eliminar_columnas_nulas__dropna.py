"""
Objetivo: eliminar columnas que son todas nulas
Referencia: dropna
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Eliminar columnas vacías
df_limpio = df.dropna(axis=1, how="all")

print(f"Columnas originales: {len(df.columns)}")
print(f"Columnas después: {len(df_limpio.columns)}")

"""output
Columnas originales: 8
Columnas después: 8
"""