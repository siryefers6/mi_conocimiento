"""
Objetivo: normalizar texto en una columna
Referencia: str
Tipo: propiedad
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Convertir producto a minúsculas y eliminar espacios
df["producto_limpio"] = df["producto"].str.lower().str.strip()

print(df[["producto", "producto_limpio"]].head())

"""output
            producto       producto_limpio
0       Laptop ASUS       laptop asis
1     Mouse Logitech    mouse logitech
2    Teclado Mecánico   teclado mecánico
3       Monitor LG 24      monitor lg 24
4    Escritorio Gamer   escritorio gamer
"""