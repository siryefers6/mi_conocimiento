"""
Objetivo: contar la frecuencia de valores en una columna
Referencia: value_counts
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

resultado = df["categoria"].value_counts()

print(resultado)

"""output
Accesorios     10
Electrónica     4
Muebles         3
Equipos         2
Name: categoria, dtype: int64
"""