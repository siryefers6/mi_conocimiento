"""
Objetivo: contar valores únicos en cada columna
Referencia: nunique
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

resultado = df.nunique()

print(resultado)

"""output
fecha          20
producto_id    14
producto       14
categoria       4
precio         14
stock          12
descuento       6
cliente_id     15
dtype: int64
"""