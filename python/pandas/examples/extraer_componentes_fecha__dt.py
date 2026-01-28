"""
Objetivo: extraer componentes de una columna fecha
Referencia: dt
Tipo: propiedad
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv", parse_dates=["fecha"])

# Extraer componentes de fecha
df["año"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["dia"] = df["fecha"].dt.day

print(df[["fecha", "año", "mes", "dia"]].head())

"""output
       fecha      año  mes  dia
0 2024-01-01  2024   1    1
1 2024-01-02  2024   1    2
2 2024-01-03  2024   1    3
3 2024-01-04  2024   1    4
4 2024-01-05  2024   1    5
"""