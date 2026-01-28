"""
Objetivo: filtrar filas por fecha
Referencia: loc
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv", parse_dates=["fecha"])

# Filtrar registros después de 2024-01-10
resultado = df.loc[df["fecha"] >= "2024-01-10"]

print(resultado[["fecha", "producto", "precio"]].head())

"""output
        fecha           producto    precio
10 2024-01-11      Laptop ASUS  1200.00
11 2024-01-12  Mouse Logitech    25.99
12 2024-01-13 Micrófono USB    60.00
13 2024-01-14 Escritorio Gamer   450.00
14 2024-01-15  Monitor Dell 27   500.00
"""