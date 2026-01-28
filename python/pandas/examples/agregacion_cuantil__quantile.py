"""
Objetivo: Obtener percentiles (cuantiles) de una columna
Referencia: quantile
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Cuartiles de edad
resultado = df['edad'].quantile([0.25, 0.5, 0.75])
print("Cuartiles de edad:")
print(resultado)

# Percentil 90 de salario
p90 = df['salario'].quantile(0.9)
print(f"\nPercentil 90 de salario: ${p90:,.2f}")

"""output
Cuartiles de edad:
0.25    29.75
0.50    33.00
0.75    42.50
Name: edad, dtype: float64

Percentil 90 de salario: $88,800.00
"""
