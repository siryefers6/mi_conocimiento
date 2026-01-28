"""
Objetivo: contar valores no nulos en cada columna
Referencia: count
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

resultado = df.count()

print(resultado)

"""output
fecha         20
producto_id   20
producto      20
categoria     20
precio        20
stock         20
descuento     20
cliente_id    20
dtype: int64
"""