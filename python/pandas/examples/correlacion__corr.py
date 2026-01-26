"""
Objetivo: Calcular la correlación entre columnas numéricas
Referencia: corr
Tipo: metodo
Nivel: intermedio
"""

import pandas as pd

# Carga de datos
df = pd.read_csv("datasets/ventas.csv")

# Limpieza: convertir columnas numéricas a float y rellenar nulos
df['precio'] = df['precio'].replace(r'[\$, USD]', '', regex=True).astype(float)
df['ventas'] = df['ventas'].fillna(0)
df['stock'] = df['stock'].fillna(0)
df['descuento'] = df['descuento'].fillna(0)

# Correlación entre columnas numéricas
correlaciones = df[['precio', 'ventas', 'stock', 'descuento']].corr()

# Resultado
print(correlaciones)

"""output
             precio    ventas     stock  descuento
precio     1.000000 -0.371247 -0.372019   0.450722
ventas    -0.371247  1.000000  0.926267  -0.510659
stock     -0.372019  0.926267  1.000000  -0.531911
descuento  0.450722 -0.510659 -0.531911   1.000000
"""
