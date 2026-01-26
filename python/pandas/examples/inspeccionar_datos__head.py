"""
Objetivo: inspeccionar las primeras filas de un DataFrame
Referencia: head
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# transformación: mostrar las primeras filas
resultado = df.head()

# resultado
print(resultado)

"""output
        fecha  producto_id    producto   categoria precio  stock  ventas   canal  descuento cliente_id
0  2024-01-01          101      Laptop  tecnologia   1200   10.0     5.0  online       0.10       C001
1  2024-01-02          102       Mouse  tecnologia     25   50.0    20.0  tienda        NaN       C002
2  2024-01-03          103     Teclado  tecnologia     45    NaN    15.0  online       0.05       C003
3  2024-01-04          104       Silla     oficina    300    5.0     2.0  tienda       0.15        NaN
4  2024-01-05          105  Escritorio     oficina    450    3.0     1.0  online       0.20       C005
"""
