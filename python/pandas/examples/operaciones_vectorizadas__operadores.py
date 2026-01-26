"""
Objetivo: Realizar operaciones vectorizadas para crear nuevas columnas
Referencia: +,-,*,/
Tipo: operador
Nivel: básico
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: calcular ingreso total por producto (precio * ventas)
df['precio'] = df['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df['ventas'] = df['ventas'].fillna(0)
df['ingreso_total'] = df['precio'] * df['ventas']

# Resultado
print(df[['producto', 'precio', 'ventas', 'ingreso_total']])

"""output
     producto  precio  ventas  ingreso_total
0      Laptop  1200.0     5.0         6000.0
1       Mouse    25.0    20.0          500.0
2     Teclado    45.0    15.0          675.0
3       Silla   300.0     2.0          600.0
4  Escritorio   450.0     1.0          450.0
5     Monitor   500.0     4.0         2000.0
6   Impresora   250.0     0.0            0.0
7  Cable HDMI    15.0    60.0          900.0
8      Webcam    85.0     0.0            0.0
9      Router   120.0     7.0          840.0
"""
