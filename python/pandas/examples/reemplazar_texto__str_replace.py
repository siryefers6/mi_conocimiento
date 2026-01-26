"""
Objetivo: reemplazar texto o patrones dentro de una columna
Referencia: str.replace
Tipo: metodo
Nivel: basico-intermedio
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# asegurar tipo texto
df["categoria"] = df["categoria"].astype(str)

# normalizar valores inconsistentes
df["categoria"] = df["categoria"].str.replace(
    "Tecnología", "Tecnologia", regex=False
)

# resultado
print(df["categoria"].unique())

"""output
['tecnologia' 'oficina' 'accesorios']
"""
