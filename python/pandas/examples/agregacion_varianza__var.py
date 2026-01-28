"""
Objetivo: Calcular varianza de una columna
Referencia: var
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Varianza de edades
resultado = df['edad'].var()
print(f"Varianza de edad: {resultado:.2f}")

# Varianza de salarios
resultado_salario = df['salario'].var()
print(f"Varianza de salario: {resultado_salario:,.2f}")

"""output
Varianza de edad: 109.21
Varianza de salario: 259,122,666.67
"""
