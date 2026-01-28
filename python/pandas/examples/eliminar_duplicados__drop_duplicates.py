"""
Objetivo: eliminar filas duplicadas del DataFrame
Referencia: drop_duplicates
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Eliminar duplicados por producto_id
df_unico = df.drop_duplicates(subset=["producto_id"], keep="first")

print(f"Filas originales: {len(df)}")
print(f"Filas únicas: {len(df_unico)}")
print()
print(df_unico[["producto_id", "producto"]].head())

"""output
Filas originales: 20
Filas únicas: 14

    producto_id         producto
0           101      Laptop ASUS
1           102  Mouse Logitech
2           103 Teclado Mecánico
3           104    Monitor LG 24
4           105 Escritorio Gamer
"""