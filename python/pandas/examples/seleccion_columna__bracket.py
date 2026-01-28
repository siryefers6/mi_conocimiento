"""
Objetivo: Seleccionar una columna completa del DataFrame
Referencia: []
Tipo: operador
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Seleccionar una columna
resultado = df['nombre']
print(resultado.head())

"""output
0        Juan
1       María
2      Carlos
3         Ana
4       Pedro
Name: nombre, dtype: object
"""
