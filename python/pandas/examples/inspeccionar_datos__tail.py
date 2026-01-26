"""
Objetivo: inspeccionar las últimas filas de un DataFrame
Referencia: tail
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: mostrar las últimas filas
resultado = df.tail()

# resultado
print(resultado)

"""output
        fecha  producto_id    producto   categoria   precio  stock  ventas   canal  descuento cliente_id
5  2024-01-06          106     Monitor  tecnologia  500 USD    8.0     4.0  online       0.10       C006
6  2024-01-07          107   Impresora     oficina      250    0.0     0.0  tienda       0.00       C007
7  2024-01-08          108  Cable HDMI  accesorios       15  100.0    60.0  online        NaN       C008
8  2024-01-09          109      Webcam  accesorios       85   20.0     NaN  online       0.05       C009
9  2024-01-10          110      Router  tecnologia      120   15.0     7.0  tienda       0.10       C010
"""
