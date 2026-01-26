"""
Objetivo: Combinar dos DataFrames usando una columna clave
Referencia: merge
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df1 = pd.read_csv("datasets/ventas.csv").head(5)  # Primeros 5 registros
df2 = pd.read_csv("datasets/ventas.csv")[['producto_id', 'cliente_id']].tail(5)  # Últimos 5 registros

# Limpieza: convertir precio a float
df1['precio'] = df1['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df1['ventas'] = df1['ventas'].fillna(0)
df2['cliente_id'] = df2['cliente_id'].fillna('Desconocido')

# Merge (left join) por columna 'producto_id'
df_merge = df1.merge(df2, on='producto_id', how='left', suffixes=('_df1','_df2'))

# Resultado
print(df_merge[['producto_id', 'producto', 'cliente_id_df1', 'cliente_id_df2']])

"""output
   producto_id    producto cliente_id_df1 cliente_id_df2
0          101      Laptop           C001            NaN
1          102       Mouse           C002            NaN
2          103     Teclado           C003            NaN
3          104       Silla            NaN            NaN
4          105  Escritorio           C005            NaN
"""
