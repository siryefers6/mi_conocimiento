"""
Objetivo: acceder a un valor específico usando posición numérica
Referencia: iat
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# acceso por posición (fila, columna)
valor = df.iat[0, 2]

# resultado
print(valor)

"""output
Laptop
"""
