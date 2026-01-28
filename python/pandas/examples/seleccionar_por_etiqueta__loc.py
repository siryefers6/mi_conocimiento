"""
Objetivo: seleccionar filas y columnas por etiqueta
Referencia: loc
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Seleccionar fila 0, columna producto
valor = df.loc[0, "producto"]
print(f"Fila 0, Producto: {valor}")

# Seleccionar filas 0-2, columnas específicas
resultado = df.loc[0:2, ["producto", "precio"]]
print()
print(resultado)

"""output
Fila 0, Producto: Laptop ASUS

           producto    precio
0       Laptop ASUS   1200.00
1     Mouse Logitech     25.99
2    Teclado Mecánico     85.50
"""