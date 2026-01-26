"""
Objetivo: eliminar registros duplicados
Referencia: drop_duplicates
Tipo: metodo
Nivel: basico-intermedio
Dataset: ventas.csv
"""

import pandas as pd

# cargar dataset
df = pd.read_csv("datasets/ventas.csv")

# simular duplicados (caso didáctico)
df_duplicado = pd.concat([df, df.iloc[[1]]], ignore_index=True)

print("Filas antes:", len(df_duplicado))

# eliminar duplicados completos
df_limpio = df_duplicado.drop_duplicates()

print("Filas después:", len(df_limpio))

"""output
Filas antes: 11
Filas después: 10
"""
