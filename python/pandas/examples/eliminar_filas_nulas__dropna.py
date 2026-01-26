"""
Objetivo: eliminar filas que contienen valores nulos
Referencia: dropna
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# eliminación de filas con al menos un valor nulo
df_limpio = df.dropna()

# resultado
print(df_limpio)

"""output
        fecha  producto_id    producto   categoria   precio  stock  ventas   canal  descuento cliente_id
0  2024-01-01          101      Laptop  tecnologia     1200   10.0     5.0  online        0.1       C001
4  2024-01-05          105  Escritorio     oficina      450    3.0     1.0  online        0.2       C005
5  2024-01-06          106     Monitor  tecnologia  500 USD    8.0     4.0  online        0.1       C006
6  2024-01-07          107   Impresora     oficina      250    0.0     0.0  tienda        0.0       C007
9  2024-01-10          110      Router  tecnologia      120   15.0     7.0  tienda        0.1       C010
"""
