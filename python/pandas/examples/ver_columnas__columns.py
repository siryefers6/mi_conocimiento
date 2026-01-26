"""
Objetivo: listar los nombres de las columnas del DataFrame
Referencia: columns
Tipo: atributo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: obtener columnas
columnas = df.columns

# resultado
print(columnas)

"""output
Index(['fecha', 'producto_id', 'producto', 'categoria', 'precio', 'stock',
       'ventas', 'canal', 'descuento', 'cliente_id'],
      dtype='object')
"""
