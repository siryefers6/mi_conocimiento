"""
Objetivo: Calcular cambio porcentual entre filas
Referencia: pct_change
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos de ventas
df = pd.read_csv('../datasets/ventas.csv')

# Agrupar por fecha y sumar ventas
df['fecha_venta'] = pd.to_datetime(df['fecha_venta'])
ventas_por_dia = df.groupby('fecha_venta')['precio_unitario'].sum().reset_index()

# Calcular cambio porcentual
ventas_por_dia['cambio_pct'] = ventas_por_dia['precio_unitario'].pct_change() * 100

print(ventas_por_dia)

"""output
  fecha_venta  precio_unitario  cambio_pct
0  2024-01-05          100.00         NaN
1  2024-01-12          250.50      150.50
2  2024-01-15          500.00       99.40
3  2024-01-20          100.00      -80.00
4  2024-02-03         1200.00     1100.00
5  2024-02-10           75.50     -93.71
6  2024-02-18          500.00      562.58
7  2024-02-25         1200.00      140.00
8  2024-03-02         2505.00      108.75
9  2024-03-10          100.00     -96.01
10 2024-03-15          528.50      428.50
11 2024-03-20          100.00     -81.07
"""
