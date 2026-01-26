"""
Objetivo: Agrupar datos por una columna para análisis agregado
Referencia: groupby
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: agrupar por categoría y sumar ventas
df_ventas_categoria = df.groupby('categoria')['ventas'].sum().reset_index()

# Resultado
print(df_ventas_categoria)

"""output
    categoria  ventas
0  accesorios    60.0
1     oficina     3.0
2  tecnologia    51.0
"""
