"""
Objetivo: Restar dos columnas numéricas
Referencia: -
Tipo: operador
Nivel: basico
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'producto': ['Camiseta', 'Pantalón', 'Zapatos'],
    'precio_original': [50, 100, 150],
    'descuento': [10, 20, 25]
}
df = pd.DataFrame(data)

# Restar columnas
df['precio_final'] = df['precio_original'] - df['descuento']
print(df)

"""output
      producto  precio_original  descuento  precio_final
0      Camiseta               50         10            40
1       Pantalón              100         20            80
2       Zapatos               150         25           125
"""
