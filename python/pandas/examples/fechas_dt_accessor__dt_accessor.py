"""
Objetivo: Acceder a componentes de fecha (año, mes, día, etc.)
Referencia: .dt
Tipo: accessor
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/clima.csv')

# Convertir columna a datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Acceder a componentes
print("Año:", df['fecha'].dt.year.head())
print("\nMes:", df['fecha'].dt.month.head())
print("\nDía:", df['fecha'].dt.day.head())

"""output
Año: 0    2024
1    2024
2    2024
3    2024
4    2024
Name: fecha, dtype: int64

Mes: 0    1
1    1
2    1
3    1
4    1
Name: fecha, dtype: int64

Día: 0    1
1    2
2    3
3    4
4    5
Name: fecha, dtype: int64
"""
