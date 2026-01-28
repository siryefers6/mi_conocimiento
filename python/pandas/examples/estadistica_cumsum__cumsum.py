"""
Objetivo: Calcular suma acumulada de valores
Referencia: cumsum
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos de ventas
data = {
    'mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'ventas': [1000, 1500, 1200, 1800, 2000]
}
df = pd.DataFrame(data)

# Calcular suma acumulada
df['ventas_acumuladas'] = df['ventas'].cumsum()

print(df)

"""output
       mes  ventas  ventas_acumuladas
0    Enero    1000               1000
1 Febrero    1500               2500
2    Marzo    1200               3700
3    Abril    1800               5500
4     Mayo    2000               7500
"""
