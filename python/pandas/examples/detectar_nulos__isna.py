"""
Objetivo: detectar valores nulos en el DataFrame
Referencia: isna
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Detectar nulos por columna
resultado = df.isna().sum()

print(resultado)

"""output
fecha         0
producto_id   0
producto      0
categoria     0
precio        0
stock         0
descuento     0
cliente_id    0
dtype: int64
"""