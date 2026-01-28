"""
Objetivo: reemplazar texto en una columna
Referencia: str.replace
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Reemplazar "ASUS" con "ASus" (estandarizar marca)
df["producto_std"] = df["producto"].str.replace("ASUS", "ASus")

print(df[["producto", "producto_std"]].head())

"""output
         producto     producto_std
0    Laptop ASUS    Laptop ASus
1  Mouse Logitech  Mouse Logitech
2 Teclado Mecánico Teclado Mecánico
3   Monitor LG 24   Monitor LG 24
4 Escritorio Gamer Escritorio Gamer
"""