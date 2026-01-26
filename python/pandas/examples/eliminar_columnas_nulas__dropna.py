"""
Objetivo: eliminar columnas que contienen valores nulos
Referencia: dropna(axis=1)
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# eliminación de columnas con al menos un valor nulo
df_limpio = df.dropna(axis=1)

# resultado
print(df_limpio.columns)

"""output
Index(['fecha', 'producto_id', 'producto', 'categoria', 'precio', 'canal'], dtype='object')
"""
