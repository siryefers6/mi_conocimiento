"""
Objetivo: reemplazar valores específicos en un DataFrame
Referencia: replace
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# reemplazar valores mal formateados en la columna precio
df["precio"] = df["precio"].replace({
    "500 USD": 500,
    "1200": 1200
})

# convertir a numérico cuando sea posible
df["precio"] = pd.to_numeric(df["precio"], errors="coerce")

# resultado
print(df[["producto", "precio"]])

"""output
     producto  precio
0      Laptop    1200
1       Mouse      25
2     Teclado      45
3       Silla     300
4  Escritorio     450
5     Monitor     500
6   Impresora     250
7  Cable HDMI      15
8      Webcam      85
9      Router     120
"""
