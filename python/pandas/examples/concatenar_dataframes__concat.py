"""
Objetivo: concatenar múltiples DataFrames
Referencia: concat
Tipo: funcion
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Dividir y concatenar
df1 = df.head(10)
df2 = df.tail(10)

resultado = pd.concat([df1, df2], ignore_index=True)

print(f"Filas df1: {len(df1)}")
print(f"Filas df2: {len(df2)}")
print(f"Filas resultado: {len(resultado)}")

"""output
Filas df1: 10
Filas df2: 10
Filas resultado: 20
"""