"""
Objetivo: agrupar datos por una columna
Referencia: groupby
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Agrupar por categoría y sumar precio
resultado = df.groupby("categoria")["precio"].sum().sort_values(ascending=False)

print(resultado)

"""output
categoria
Electrónica    8100.00
Muebles        1350.00
Accesorios      437.48
Name: precio, dtype: float64
"""