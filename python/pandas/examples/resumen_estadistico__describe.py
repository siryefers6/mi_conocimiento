"""
Objetivo: obtener estadísticas descriptivas de columnas numéricas
Referencia: describe
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: estadísticas descriptivas
resumen = df.describe()

# resultado
print(resumen)

"""output
       producto_id       stock     ventas  descuento
count     10.00000    9.000000   9.000000   8.000000
mean     105.50000   23.444444  12.666667   0.093750
std        3.02765   32.357809  18.960485   0.062321
min      101.00000    0.000000   0.000000   0.000000
25%      103.25000    5.000000   2.000000   0.050000
50%      105.50000   10.000000   5.000000   0.100000
75%      107.75000   20.000000  15.000000   0.112500
max      110.00000  100.000000  60.000000   0.200000
"""
