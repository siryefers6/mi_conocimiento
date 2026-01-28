"""
Objetivo: Calcular valor central (mediana) de una columna
Referencia: median
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Mediana de edades
resultado = df['edad'].median()
print(f"Edad mediana: {resultado:.1f} años")

# Mediana de salarios
resultado_salario = df['salario'].median()
print(f"Salario mediano: ${resultado_salario:,.2f}")

"""output
Edad mediana: 33.0 años
Salario mediano: $58,000.00
"""
