"""
Objetivo: Calcular la covarianza entre columnas numéricas
Referencia: cov
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

# Covarianza entre columnas numéricas
covarianza = df[['precio', 'ventas', 'stock', 'descuento']].cov()

# Resultado
print(covarianza)

"""output
                  precio       ventas        stock  descuento
precio     130610.000000 -2457.888889 -4221.000000  11.027778
ventas      -2457.888889   335.600000   532.733333  -0.633333
stock       -4221.000000   532.733333   985.655556  -1.130556
descuento      11.027778    -0.633333    -1.130556   0.004583
"""
