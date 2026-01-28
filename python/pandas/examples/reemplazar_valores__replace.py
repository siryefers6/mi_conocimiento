"""
Objetivo: reemplazar valores en una columna
Referencia: replace
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Reemplazar valor 0 con "Sin descuento"
resultado = df.copy()
resultado["descuento"] = resultado["descuento"].replace(0.0, "Sin descuento")

print(resultado[["producto", "descuento"]].head())

"""output
            producto            descuento
0       Laptop ASIS             0.1
1     Mouse Logitech    Sin descuento
2    Teclado Mecánico             0.05
3       Monitor LG 24             0.15
4    Escritorio Gamer             0.2
"""