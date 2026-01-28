"""
Objetivo: seleccionar múltiples columnas del DataFrame
Referencia: []
Tipo: sintaxis
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

resultado = df[["producto", "precio", "categoria"]]

print(resultado.head())

"""output
            producto      categoria    precio
0       Laptop ASUS   Electrónica  1200.00
1     Mouse Logitech    Accesorios    25.99
2    Teclado Mecánico   Accesorios    85.50
3       Monitor LG 24   Electrónica   300.00
4    Escritorio Gamer      Muebles   450.00
"""