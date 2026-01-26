"""
Objetivo: cargar un archivo CSV en un DataFrame
Referencia: read_csv
Tipo: funcion
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# resultado
print(df)

"""output
        fecha  producto_id    producto   categoria   precio  stock  ventas   canal  descuento cliente_id
0  2024-01-01          101      Laptop  tecnologia     1200   10.0     5.0  online       0.10       C001
1  2024-01-02          102       Mouse  tecnologia       25   50.0    20.0  tienda        NaN       C002
2  2024-01-03          103     Teclado  tecnologia       45    NaN    15.0  online       0.05       C003
3  2024-01-04          104       Silla     oficina      300    5.0     2.0  tienda       0.15        NaN
4  2024-01-05          105  Escritorio     oficina      450    3.0     1.0  online       0.20       C005
5  2024-01-06          106     Monitor  tecnologia  500 USD    8.0     4.0  online       0.10       C006
6  2024-01-07          107   Impresora     oficina      250    0.0     0.0  tienda       0.00       C007
7  2024-01-08          108  Cable HDMI  accesorios       15  100.0    60.0  online        NaN       C008
8  2024-01-09          109      Webcam  accesorios       85   20.0     NaN  online       0.05       C009
9  2024-01-10          110      Router  tecnologia      120   15.0     7.0  tienda       0.10       C010
"""
