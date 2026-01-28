"""
Objetivo: crear tabla pivote de datos
Referencia: pivot_table
Tipo: funcion
Nivel: avanzado
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Tabla pivote: categoría x cliente
resultado = pd.pivot_table(df, values="precio", index="categoria", aggfunc="sum")

print(resultado)

"""output
               precio
categoria
Accesorios      437.48
Electrónica    8100.00
Muebles        1350.00
"""