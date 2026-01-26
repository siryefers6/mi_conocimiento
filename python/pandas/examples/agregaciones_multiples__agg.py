"""
Objetivo: Aplicar múltiples agregaciones a diferentes columnas de un grupo
Referencia: agg
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Transformación: limpiar columna precio y convertir a float
df['precio'] = df['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df['ventas'] = df['ventas'].fillna(0)

# Agrupar por categoría y aplicar varias funciones a columnas diferentes
df_agregaciones_multiples = df.groupby('categoria').agg({
    'ventas': 'sum',      # total de ventas por categoría
    'precio': 'mean'      # precio promedio por categoría
}).reset_index()

# Resultado
print(df_agregaciones_multiples)

"""output
    categoria  ventas      precio
0  accesorios    60.0   50.000000
1     oficina     3.0  333.333333
2  tecnologia    51.0  378.000000
"""
