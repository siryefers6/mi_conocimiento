"""
Objetivo: Dividir dos columnas numéricas
Referencia: /
Tipo: operador
Nivel: basico
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'producto': ['Tarta', 'Pizza', 'Pastel'],
    'total_precio': [60, 100, 80],
    'porciones': [12, 8, 10]
}
df = pd.DataFrame(data)

# Dividir columnas
df['precio_porcion'] = df['total_precio'] / df['porciones']
print(df)

"""output
  producto  total_precio  porciones  precio_porcion
0     Tarta            60         12             5.0
1     Pizza           100          8            12.5
2    Pastel            80         10             8.0
"""
