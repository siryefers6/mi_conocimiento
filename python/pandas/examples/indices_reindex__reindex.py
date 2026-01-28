"""
Objetivo: Cambiar/reordenar índice de un DataFrame
Referencia: reindex
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos pequeños
data = {
    'nombre': ['Juan', 'María', 'Carlos'],
    'edad': [28, 34, 45]
}
df = pd.DataFrame(data, index=['A', 'B', 'C'])

# Reindexar con nuevo orden
nuevo_orden = ['C', 'A', 'B']
df_reindexado = df.reindex(nuevo_orden)

print("DataFrame reindexado:")
print(df_reindexado)

# Reindexar agregando nuevos índices
nuevo_indice = ['A', 'B', 'C', 'D']
df_expandido = df.reindex(nuevo_indice)

print("\nDataFrame expandido con índice faltante:")
print(df_expandido)

"""output
DataFrame reindexado:
  nombre  edad
C Carlos    45
A   Juan    28
B  María    34

DataFrame expandido con índice faltante:
  nombre  edad
A   Juan    28
B  María    34
C Carlos    45
D    NaN   NaN
"""
