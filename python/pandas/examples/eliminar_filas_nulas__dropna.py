"""
Objetivo: eliminar filas que contienen valores nulos
Referencia: dropna
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Eliminar filas con valores nulos
df_limpio = df.dropna()

print(f"Filas originales: {len(df)}")
print(f"Filas después de dropna: {len(df_limpio)}")

"""output
Filas originales: 20
Filas después de dropna: 20
"""