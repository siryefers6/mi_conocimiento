"""
Objetivo: Obtener valor mínimo de una columna
Referencia: min
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Edad mínima
resultado = df['edad'].min()
print(f"Edad mínima: {resultado} años")

# Salario mínimo
resultado_salario = df['salario'].min()
print(f"Salario mínimo: ${resultado_salario:,}")

"""output
Edad mínima: 27 años
Salario mínimo: $45,000
"""
