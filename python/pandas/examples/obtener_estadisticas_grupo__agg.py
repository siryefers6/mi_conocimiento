"""
Objetivo: obtener múltiples estadísticas por grupo
Referencia: agg
Tipo: metodo
Nivel: avanzado
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Estadísticas por categoría
resultado = df.groupby("categoria").agg({
    "precio": ["min", "max", "mean"],
    "stock": "sum",
    "producto": "count"
})

print(resultado)

"""output
              precio             stock producto
                 min      max     mean  sum    count
categoria
Accesorios      15.0   85.50   43.748   180        4
Electrónica     25.99  1200.0  405.000   30        6
Muebles        450.0   450.00  450.000    5        2
"""