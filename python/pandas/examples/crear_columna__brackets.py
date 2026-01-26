"""
Objetivo: Crear una nueva columna calculada en el DataFrame
Referencia: []
Tipo: sintaxis
Nivel: básico
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: crear columna de ingreso por producto
df['ingreso'] = df['precio'].replace(r'[\$, USD]', '', regex=True).astype(float) * df['ventas'].fillna(0)

# Resultado
print(df[['producto', 'precio', 'ventas', 'ingreso']])

"""output
     producto   precio  ventas  ingreso
0      Laptop     1200     5.0   6000.0
1       Mouse       25    20.0    500.0
2     Teclado       45    15.0    675.0
3       Silla      300     2.0    600.0
4  Escritorio      450     1.0    450.0
5     Monitor  500 USD     4.0   2000.0
6   Impresora      250     0.0      0.0
7  Cable HDMI       15    60.0    900.0
8      Webcam       85     NaN      0.0
9      Router      120     7.0    840.0
"""
