"""
Objetivo: Sumar dos columnas numéricas
Referencia: +
Tipo: operador
Nivel: basico
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'producto': ['Laptop', 'Monitor', 'Teclado'],
    'precio_base': [1000, 500, 150],
    'impuesto': [200, 100, 30]
}
df = pd.DataFrame(data)

# Sumar columnas
df['precio_final'] = df['precio_base'] + df['impuesto']
print(df)

"""output
  producto  precio_base  impuesto  precio_final
0    Laptop         1000        200          1200
1   Monitor          500        100           600
2   Teclado          150         30           180
"""
