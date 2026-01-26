"""
Objetivo: Unir dos DataFrames usando los índices
Referencia: join
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df1 = pd.read_csv("datasets/ventas.csv").head(5).set_index('producto_id')  # Primeros 5 registros
df2 = pd.read_csv("datasets/ventas.csv")[['producto_id', 'cliente_id']].tail(5).set_index('producto_id')  # Últimos 5 registros

# Limpieza: convertir precio a float
df1['precio'] = df1['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df1['ventas'] = df1['ventas'].fillna(0)
df2['cliente_id'] = df2['cliente_id'].fillna('Desconocido')

# Join por índice (left join) con sufijo para evitar conflictos
df_join = df1.join(df2, how='left', rsuffix='_df2')

# Renombrar la columna resultante si se creó con sufijo
if 'cliente_id_df2' in df_join.columns:
    df_join.rename(columns={'cliente_id_df2': 'cliente_id'}, inplace=True)

# Resultado
print(df_join[['producto', 'ventas', 'precio', 'cliente_id']])

"""output
               producto  ventas  precio cliente_id cliente_id
producto_id
101              Laptop     5.0  1200.0       C001        NaN
102               Mouse    20.0    25.0       C002        NaN
103             Teclado    15.0    45.0       C003        NaN
104               Silla     2.0   300.0        NaN        NaN
105          Escritorio     1.0   450.0       C005        NaN
"""
