"""
Objetivo: acceder a un valor específico usando etiquetas
Referencia: at
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

# carga de datos
df = pd.read_csv("datasets/ventas.csv")

# acceso a una celda específica
valor = df.at[0, "producto"]

# resultado
print(valor)

"""output
Laptop
"""
