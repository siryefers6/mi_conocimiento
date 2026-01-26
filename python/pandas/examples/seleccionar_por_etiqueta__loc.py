"""
Objetivo: seleccionar filas y columnas usando etiquetas
Referencia: loc
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# selección por etiquetas
seleccion = df.loc[0:3, ["producto", "categoria", "ventas"]]

# resultado
print(seleccion)

"""output
  producto   categoria  ventas
0   Laptop  tecnologia     5.0
1    Mouse  tecnologia    20.0
2  Teclado  tecnologia    15.0
3    Silla     oficina     2.0
"""
