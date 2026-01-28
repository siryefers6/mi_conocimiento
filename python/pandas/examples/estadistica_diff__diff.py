"""
Objetivo: Calcular diferencias entre filas consecutivas
Referencia: diff
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos de series de tiempo
data = {
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'temperatura': [10, 12, 15, 13]
}
df = pd.DataFrame(data)

# Calcular diferencia entre filas
df['cambio_temp'] = df['temperatura'].diff()

print(df)

"""output
      fecha  temperatura  cambio_temp
0 2024-01-01           10          NaN
1 2024-01-02           12          2.0
2 2024-01-03           15          3.0
3 2024-01-04           13         -2.0
"""
