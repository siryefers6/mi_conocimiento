"""
Objetivo: ver los nombres de todas las columnas
Referencia: columns
Tipo: atributo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

columnas = df.columns

print(list(columnas))
print()
print(f"Total de columnas: {len(columnas)}")

"""output
['fecha', 'producto_id', 'producto', 'categoria', 'precio', 'stock', 'descuento', 'cliente_id']

Total de columnas: 8
"""