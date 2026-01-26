"""
Objetivo: eliminar espacios en blanco al inicio y final del texto
Referencia: str.strip
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# limpieza de espacios
df["producto"] = df["producto"].str.strip()
df["categoria"] = df["categoria"].str.strip()

# resultado
print(df[["producto", "categoria"]])

"""output
     producto   categoria
0      Laptop  tecnologia
1       Mouse  tecnologia
2     Teclado  tecnologia
3       Silla     oficina
4  Escritorio     oficina
5     Monitor  tecnologia
6   Impresora     oficina
7  Cable HDMI  accesorios
8      Webcam  accesorios
9      Router  tecnologia
"""
