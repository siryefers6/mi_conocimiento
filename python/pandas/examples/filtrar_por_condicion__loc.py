"""
Objetivo: filtrar filas usando una condición lógica
Referencia: loc
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# filtro condicional
filtro = df.loc[df["ventas"] > 10, ["producto", "ventas", "canal"]]

# resultado
print(filtro)

"""output
     producto  ventas   canal
1       Mouse    20.0  tienda
2     Teclado    15.0  online
7  Cable HDMI    60.0  online
"""
