"""
Objetivo: Filtrar filas según un rango de fechas usando loc
Referencia: loc
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: convertir fecha a datetime
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d', errors='coerce')

# Filtrar filas entre el 2024-01-03 y 2024-01-07
df_filtrado = df.loc[(df['fecha'] >= '2024-01-03') & (df['fecha'] <= '2024-01-07')]

# Resultado
print(df_filtrado[['fecha', 'producto', 'ventas']])

"""output
       fecha    producto  ventas
2 2024-01-03     Teclado    15.0
3 2024-01-04       Silla     2.0
4 2024-01-05  Escritorio     1.0
5 2024-01-06     Monitor     4.0
6 2024-01-07   Impresora     0.0
"""
