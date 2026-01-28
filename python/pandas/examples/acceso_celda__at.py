"""
Objetivo: acceder a un valor específico usando etiqueta
Referencia: at
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Acceso por etiqueta (fila, columna)
valor = df.at[0, "producto"]
print(f"Valor en [0, 'producto']: {valor}")

precio = df.at[3, "precio"]
print(f"Valor en [3, 'precio']: {precio}")

"""output
Valor en [0, 'producto']: Laptop ASUS
Valor en [3, 'precio']: 300.0
"""