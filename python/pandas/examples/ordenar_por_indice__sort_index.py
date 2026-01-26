"""
Objetivo: Ordenar un DataFrame según su índice
Referencia: sort_index
Tipo: metodo
Nivel: básico
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Limpieza: convertir precio a float
df['precio'] = df['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df['ventas'] = df['ventas'].fillna(0)

# Reordenar filas por índice (ascendente)
df_ordenado = df.sort_index()

# Resultado
print(df_ordenado[['producto', 'ventas', 'precio']])

"""output
     producto  ventas  precio
0      Laptop     5.0  1200.0
1       Mouse    20.0    25.0
2     Teclado    15.0    45.0
3       Silla     2.0   300.0
4  Escritorio     1.0   450.0
5     Monitor     4.0   500.0
6   Impresora     0.0   250.0
7  Cable HDMI    60.0    15.0
8      Webcam     0.0    85.0
9      Router     7.0   120.0
"""
