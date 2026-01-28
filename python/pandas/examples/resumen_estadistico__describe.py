"""
Objetivo: obtener estadísticas descriptivas numéricas
Referencia: describe
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

resultado = df.describe()

print(resultado)

"""output
       producto_id      precio       stock   descuento
count         20.0   20.000000        20.0        20.0
mean         107.6   341.045000        26.5         0.089
std            5.2   446.235680        24.9         0.081
min          101.0    15.000000         0.0         0.000
25%          105.5   150.000000         7.5         0.000
50%          108.0   250.000000        18.5         0.075
75%          110.5   455.000000        30.0         0.125
max          114.0  1200.000000       100.0         0.250
"""