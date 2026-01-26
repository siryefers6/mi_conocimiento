"""
Objetivo: rellenar valores nulos con un valor específico
Referencia: fillna
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# rellenar valores nulos con valores definidos
df["descuento"] = df["descuento"].fillna(0)
df["stock"] = df["stock"].fillna(df["stock"].mean())
df["ventas"] = df["ventas"].fillna(0)

# resultado
print(df[["stock", "ventas", "descuento"]])

"""output
        stock  ventas  descuento
0   10.000000     5.0       0.10
1   50.000000    20.0       0.00
2   23.444444    15.0       0.05
3    5.000000     2.0       0.15
4    3.000000     1.0       0.20
5    8.000000     4.0       0.10
6    0.000000     0.0       0.00
7  100.000000    60.0       0.00
8   20.000000     0.0       0.05
9   15.000000     7.0       0.10
"""
