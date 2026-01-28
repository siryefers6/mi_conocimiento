"""
Objetivo: Calcular promedio de una columna
Referencia: mean
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Promedio de edades
resultado = df['edad'].mean()
print(f"Edad promedio: {resultado:.1f} años")

# Promedio de salarios
resultado_salario = df['salario'].mean()
print(f"Salario promedio: ${resultado_salario:,.2f}")

"""output
Edad promedio: 35.9 años
Salario promedio: $61,600.00
"""
