"""
Objetivo: Combinar dos DataFrames manteniendo filas de la izquierda
Referencia: merge(how='left')
Tipo: función
Nivel: intermedio
"""

import pandas as pd

# Crear datos de ejemplo
df_izq = pd.DataFrame({
    'id': [1, 2, 3],
    'nombre': ['Juan', 'María', 'Carlos']
})

df_der = pd.DataFrame({
    'id': [1, 2, 4],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia']
})

# Merge left
resultado = pd.merge(df_izq, df_der, on='id', how='left')
print(resultado)

"""output
   id     nombre      ciudad
0   1       Juan      Madrid
1   2      María   Barcelona
2   3     Carlos         NaN
"""
