"""
Objetivo: Calcular desviación estándar de una columna
Referencia: std
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Desviación estándar de edades
resultado = df['edad'].std()
print(f"Desv. estándar de edad: {resultado:.2f}")

# Desviación estándar de salarios
resultado_salario = df['salario'].std()
print(f"Desv. estándar de salario: ${resultado_salario:,.2f}")

"""output
Desv. estándar de edad: 10.45
Desv. estándar de salario: $16,097.28
"""
