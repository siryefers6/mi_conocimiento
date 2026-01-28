"""
Objetivo: contar el total de valores nulos
Referencia: isna, sum
Tipo: metodo
Nivel: basico
Dataset: ventas.csv
"""

import pandas as pd

df = pd.read_csv("datasets/ventas.csv")

# Total de nulos en el DataFrame
total_nulos = df.isna().sum().sum()
print(f"Total de valores nulos: {total_nulos}")

porcentaje = (total_nulos / (len(df) * len(df.columns))) * 100
print(f"Porcentaje: {porcentaje:.2f}%")

"""output
Total de valores nulos: 0
Porcentaje: 0.00%
"""