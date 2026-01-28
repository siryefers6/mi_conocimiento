"""
Objetivo: Obtener valor máximo de una columna
Referencia: max
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Edad máxima
resultado = df['edad'].max()
print(f"Edad máxima: {resultado} años")

# Salario máximo
resultado_salario = df['salario'].max()
print(f"Salario máximo: ${resultado_salario:,}")

"""output
Edad máxima: 55 años
Salario máximo: $95,000
"""
