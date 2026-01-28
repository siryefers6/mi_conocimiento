"""
Objetivo: calcular la matriz de correlación
Referencia: corr
Tipo: metodo
Nivel: avanzado
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Correlación entre precio y stock
resultado = df[["precio", "stock", "descuento"]].corr()

print(resultado)

"""output
              precio     stock  descuento
precio       1.000000  -0.102632   0.354938
stock       -0.102632   1.000000  -0.128925
descuento    0.354938  -0.128925   1.000000
"""