"""
Objetivo: acceder a un valor específico usando posición numérica
Referencia: iat
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Acceso por posición (fila, columna)
valor = df.iat[0, 2]
print(f"Valor en [0, 2]: {valor}")

valor2 = df.iat[4, 4]
print(f"Valor en [4, 4]: {valor2}")

"""output
Valor en [0, 2]: Laptop ASUS
Valor en [4, 4]: 450.0
"""