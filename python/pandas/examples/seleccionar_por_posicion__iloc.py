"""
Objetivo: seleccionar filas y columnas por posición numérica
Referencia: iloc
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Seleccionar fila 0, columnas 0-3
resultado = df.iloc[0, 0:4]
print(resultado)
print()

# Seleccionar filas 0-2
resultado2 = df.iloc[0:3][["fecha", "producto", "precio"]]
print(resultado2)

"""output
fecha           2024-01-01
producto_id              101
producto          Laptop ASUS
categoria         Electrónica
Name: 0, dtype: object

       fecha           producto    precio
0 2024-01-01       Laptop ASUS  1200.00
1 2024-01-02     Mouse Logitech   25.99
2 2024-01-03    Teclado Mecánico   85.50
"""