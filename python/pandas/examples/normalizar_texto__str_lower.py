"""
Objetivo: normalizar texto a minúsculas
Referencia: str.lower
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# normalizar texto
df["categoria"] = df["categoria"].str.lower()
df["canal"] = df["canal"].str.lower()

# resultado
print(df[["producto", "categoria", "canal"]])

"""output
     producto   categoria   canal
0      Laptop  tecnologia  online
1       Mouse  tecnologia  tienda
2     Teclado  tecnologia  online
3       Silla     oficina  tienda
4  Escritorio     oficina  online
5     Monitor  tecnologia  online
6   Impresora     oficina  tienda
7  Cable HDMI  accesorios  online
8      Webcam  accesorios  online
9      Router  tecnologia  tienda
"""
