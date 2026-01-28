"""
Objetivo: Crear tabla pivote con agregación
Referencia: pivot_table
Tipo: función
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/ventas.csv')

# Crear tabla pivote: ventas por producto y región
resultado = pd.pivot_table(
    df,
    values='cantidad',
    index='id_producto',
    columns='region',
    aggfunc='sum'
)

print(resultado)

"""output
region    Este  Norte  Oeste
id_producto                    
101         5.0    8.0    NaN
102         6.0    NaN    6.0
103        10.0    3.0    NaN
104         NaN    4.0    7.0
105         2.0    NaN    NaN
"""
