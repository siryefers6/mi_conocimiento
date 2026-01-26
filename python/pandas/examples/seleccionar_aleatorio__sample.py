"""
Objetivo: seleccionar filas aleatorias de un DataFrame
Referencia: sample
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# selección aleatoria de filas
muestra = df.sample(n=3, random_state=42)

# resultado
print(muestra)

"""output
        fecha  producto_id producto   categoria   precio  stock  ventas   canal  descuento cliente_id
8  2024-01-09          109   Webcam  accesorios       85   20.0     NaN  online       0.05       C009
1  2024-01-02          102    Mouse  tecnologia       25   50.0    20.0  tienda        NaN       C002
5  2024-01-06          106  Monitor  tecnologia  500 USD    8.0     4.0  online       0.10       C006
"""
