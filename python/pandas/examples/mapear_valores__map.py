"""
Objetivo: mapear valores de una columna usando diccionario
Referencia: map
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Mapear categorías a etiquetas
categoria_map = {
    "Electrónica": "HIGH-PRICE",
    "Accesorios": "MEDIUM-PRICE",
    "Muebles": "FURNITURE"
}

df["categoria_etiqueta"] = df["categoria"].map(categoria_map)

print(df[["producto", "categoria", "categoria_etiqueta"]].head())

"""output
            producto      categoria categoria_etiqueta
0       Laptop ASUS   Electrónica      HIGH-PRICE
1     Mouse Logitech    Accesorios    MEDIUM-PRICE
2    Teclado Mecánico   Accesorios    MEDIUM-PRICE
3       Monitor LG 24   Electrónica      HIGH-PRICE
4    Escritorio Gamer      Muebles        FURNITURE
"""