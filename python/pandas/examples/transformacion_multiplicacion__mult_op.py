"""
Objetivo: Multiplicar dos columnas numéricas
Referencia: *
Tipo: operador
Nivel: basico
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'producto': ['Manzana', 'Naranja', 'Plátano'],
    'cantidad': [10, 15, 20],
    'precio_unitario': [0.5, 0.75, 0.3]
}
df = pd.DataFrame(data)

# Multiplicar columnas
df['total'] = df['cantidad'] * df['precio_unitario']
print(df)

"""output
  producto  cantidad  precio_unitario  total
0   Manzana        10              0.50    5.0
1    Naranja        15              0.75   11.25
2    Plátano        20              0.30    6.0
"""
