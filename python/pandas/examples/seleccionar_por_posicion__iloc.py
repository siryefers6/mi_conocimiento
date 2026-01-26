"""
Objetivo: seleccionar filas y columnas usando índices numéricos
Referencia: iloc
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# selección por posición
seleccion = df.iloc[0:3, 0:4]

# resultado
print(seleccion)

"""output
        fecha  producto_id producto   categoria
0  2024-01-01          101   Laptop  tecnologia
1  2024-01-02          102    Mouse  tecnologia
2  2024-01-03          103  Teclado  tecnologia
"""
