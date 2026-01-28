"""
Objetivo: cargar un archivo CSV básicamente
Referencia: read_csv
Tipo: funcion
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

print(df.head())
print(f"Shape: {df.shape}")

"""output
     fecha producto_id           producto      categoria    precio  stock  descuento cliente_id
0 2024-01-01         101      Laptop ASUS   Electrónica  1200.00     10       0.10       C001
1 2024-01-02         102  Mouse Logitech    Accesorios    25.99     50       0.00       C002
2 2024-01-03         103 Teclado Mecánico   Accesorios    85.50     30       0.05       C003
3 2024-01-04         104    Monitor LG 24   Electrónica   300.00      5       0.15       C001
4 2024-01-05         105 Escritorio Gamer      Muebles   450.00      3       0.20       C005

Shape: (20, 8)
"""