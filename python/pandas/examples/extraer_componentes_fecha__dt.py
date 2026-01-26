"""
Objetivo: Extraer componentes de fecha (año, mes, día) de una columna datetime
Referencia: dt
Tipo: atributo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: convertir fecha a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')

# Extraer componentes de la fecha
df['año'] = df['fecha'].dt.year
df['mes'] = df['fecha'].dt.month
df['día'] = df['fecha'].dt.day

# Resultado
print(df[['fecha', 'año', 'mes', 'día', 'producto']])

"""output
       fecha   año  mes  día    producto
0 2024-01-01  2024    1    1      Laptop
1 2024-01-02  2024    1    2       Mouse
2 2024-01-03  2024    1    3     Teclado
3 2024-01-04  2024    1    4       Silla
4 2024-01-05  2024    1    5  Escritorio
5 2024-01-06  2024    1    6     Monitor
6 2024-01-07  2024    1    7   Impresora
7 2024-01-08  2024    1    8  Cable HDMI
8 2024-01-09  2024    1    9      Webcam
9 2024-01-10  2024    1   10      Router
"""
