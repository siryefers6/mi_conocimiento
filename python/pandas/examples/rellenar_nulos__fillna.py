"""
Objetivo: rellenar valores nulos con un valor especificado
Referencia: fillna
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Rellenar nulos en descuento con 0
df_limpio = df.fillna({"descuento": 0})

print(df_limpio[["producto", "descuento"]].head())

"""output
            producto  descuento
0       Laptop ASUS       0.10
1     Mouse Logitech       0.00
2    Teclado Mecánico       0.05
3       Monitor LG 24       0.15
4    Escritorio Gamer       0.20
"""