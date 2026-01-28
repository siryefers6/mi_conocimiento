"""
Objetivo: extraer valores que coinciden con un patrón
Referencia: str.contains
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Filtrar productos que contienen "Laptop"
resultado = df[df["producto"].str.contains("Laptop", case=False)]

print(resultado[["producto", "precio"]])

"""output
           producto    precio
0       Laptop ASUS   1200.00
10      Laptop ASUS   1200.00
11      Laptop ASUS   1200.00
"""