"""
Objetivo: filtrar filas que contengan un patrón de texto
Referencia: str.contains
Tipo: metodo
Nivel: basico-intermedio
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# asegurar texto y manejar nulos
df["producto"] = df["producto"].astype(str)

# filtrar productos que contienen 'cam'
filtro = df["producto"].str.contains("cam", case=False, na=False)
df_filtrado = df[filtro]

# resultado
print(df_filtrado[["producto", "categoria"]])

"""output
  producto   categoria
8   Webcam  accesorios
"""
