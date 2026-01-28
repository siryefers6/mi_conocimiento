"""
Objetivo: Rellenar valores nulos con un valor específico
Referencia: fillna
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos con valores faltantes
df = pd.read_csv('../datasets/frutas.csv')

# Rellenar cantidad faltante con 0
df_cantidad = df.fillna({'cantidad': 0})
print("Rellenar cantidad con 0:")
print(df_cantidad[['producto', 'cantidad']])

# Rellenar precio con el promedio
precio_promedio = df['precio'].mean()
df_precio = df.fillna({'precio': precio_promedio})
print(f"\nRellenar precio con promedio ({precio_promedio:.2f}):")
print(df_precio[['producto', 'precio']])

"""output
Rellenar cantidad con 0:
  producto  cantidad
0  Manzana       10.0
1  Plátano       15.0
2   Naranja        8.0
3  Manzana       12.0
4  Plátano        0.0
5     Uva       20.0
6   Naranja        5.0
7   Fresa         0.0
8  Manzana       14.0
9  Plátano       18.0

Rellenar precio con promedio (0.64):
  producto  precio
0  Manzana    0.50
1  Plátano    0.30
2   Naranja    0.64
3  Manzana    0.50
4  Plátano    0.30
5     Uva    1.20
6   Naranja    0.75
7   Fresa    0.80
8  Manzana    0.50
9  Plátano    0.30
"""
