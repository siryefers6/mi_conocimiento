"""
Objetivo: realizar agregaciones básicas (sum, mean, count)
Referencia: sum, mean, count
Tipo: metodo
Nivel: intermedio
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Agregaciones por categoría
resultado = df.groupby("categoria")[["precio", "stock"]].agg({
    "precio": ["sum", "mean"],
    "stock": "sum"
})

print(resultado)

"""output
               precio        stock
                sum     mean   sum
categoria
Accesorios     437.48    43.75   180
Electrónica   8100.00   405.00    30
Muebles       1350.00   450.00     5
"""