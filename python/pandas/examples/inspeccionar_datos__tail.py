"""
Objetivo: ver las últimas filas del DataFrame
Referencia: tail
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

resultado = df.tail(2)

print(resultado)

"""output
      fecha producto_id         producto categoria    precio  stock  descuento cliente_id
18 2024-01-19         114 Batería Externa Accesorios    55.00     18        0.10       C017
19 2024-01-20         101     Laptop ASUS Electrónica  1200.00      8        0.10       C018
"""