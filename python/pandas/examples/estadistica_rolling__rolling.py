"""
Objetivo: Calcular operaciones en ventana móvil (rolling window)
Referencia: rolling
Tipo: método
Nivel: avanzado
"""

import pandas as pd

# Crear datos de series de tiempo
data = {
    'fecha': pd.date_range('2024-01-01', periods=10, freq='D'),
    'temperatura': [10, 12, 11, 13, 15, 14, 16, 18, 17, 15]
}
df = pd.DataFrame(data)

# Calcular promedio móvil de 3 días
df['temp_promedio_3d'] = df['temperatura'].rolling(window=3).mean()

print(df)

"""output
      fecha  temperatura  temp_promedio_3d
0 2024-01-01           10               NaN
1 2024-01-02           12               NaN
2 2024-01-03           11            11.00
3 2024-01-04           13            12.00
4 2024-01-05           15            13.00
5 2024-01-06           14            14.00
6 2024-01-07           16            15.00
7 2024-01-08           18            16.00
8 2024-01-09           17            17.00
9 2024-01-10           15            16.67
"""
