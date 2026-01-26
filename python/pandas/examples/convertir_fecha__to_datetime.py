"""
Objetivo: Convertir una columna de texto a tipo datetime
Referencia: to_datetime
Tipo: funcion
Nivel: básico
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: convertir la columna 'fecha' a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')

# Resultado
print(df[['fecha', 'producto', 'precio']])

"""output
       fecha    producto   precio
0 2024-01-01      Laptop     1200
1 2024-01-02       Mouse       25
2 2024-01-03     Teclado       45
3 2024-01-04       Silla      300
4 2024-01-05  Escritorio      450
5 2024-01-06     Monitor  500 USD
6 2024-01-07   Impresora      250
7 2024-01-08  Cable HDMI       15
8 2024-01-09      Webcam       85
9 2024-01-10      Router      120
"""
