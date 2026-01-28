"""
Objetivo: Obtener valor más frecuente (moda) de una columna
Referencia: mode
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Moda de departamento
resultado = df['departamento'].mode()
print("Departamento más frecuente:")
print(resultado.values[0])

# Moda de edad
resultado_edad = df['edad'].mode()
print(f"\nEdades que más aparecen: {resultado_edad.values}")

"""output
Departamento más frecuente:
Ventas

Edades que más aparecen: []
"""
