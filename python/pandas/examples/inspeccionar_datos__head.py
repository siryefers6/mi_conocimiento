"""
Objetivo: ver las primeras filas del DataFrame
Referencia: head
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

resultado = df.head(3)

print(resultado)

"""output
     fecha producto_id           producto      categoria    precio  stock  descuento cliente_id
0 2024-01-01         101      Laptop ASUS   Electrónica  1200.00     10       0.10       C001
1 2024-01-02         102  Mouse Logitech    Accesorios    25.99     50       0.00       C002
2 2024-01-03         103 Teclado Mecánico   Accesorios    85.50     30       0.05       C003
"""