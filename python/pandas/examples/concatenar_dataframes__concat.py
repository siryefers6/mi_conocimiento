"""
Objetivo: Concatenar dos DataFrames en filas o columnas
Referencia: concat
Tipo: funcion
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df1 = pd.read_csv("datasets/ventas.csv").head(5)  # Primeros 5 registros
df2 = pd.read_csv("datasets/ventas.csv").tail(5)  # Últimos 5 registros

# Limpieza: convertir precio a float
df1['precio'] = df1['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df2['precio'] = df2['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df1['ventas'] = df1['ventas'].fillna(0)
df2['ventas'] = df2['ventas'].fillna(0)

# Concatenar DataFrames verticalmente (filas)
df_concatenado = pd.concat([df1, df2], axis=0).reset_index(drop=True)

# Resultado
print(df_concatenado[['producto', 'ventas', 'precio']])

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
