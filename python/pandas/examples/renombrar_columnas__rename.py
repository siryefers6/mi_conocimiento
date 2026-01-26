"""
Objetivo: estandarizar nombres de columnas
Referencia: rename
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# cargar dataset
df = pd.read_csv("datasets/ventas.csv")

# columnas originales
print(df.columns.tolist())

# estandarizar nombres (snake_case)
df = df.rename(columns={
    "producto_id": "id_producto"
})

# resultado
print(df.columns.tolist())

"""
output
['fecha', 'producto_id', 'producto', 'categoria', 'precio', 'stock', 'ventas', 'canal', 'descuento', 'cliente_id']
['fecha', 'id_producto', 'producto', 'categoria', 'precio', 'stock', 'ventas', 'canal', 'descuento', 'cliente_id']
"""
