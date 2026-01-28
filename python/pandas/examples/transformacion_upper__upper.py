"""
Objetivo: Convertir string a mayúsculas
Referencia: .str.upper
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Convertir a mayúsculas
resultado = df['nombre'].str.upper()
print(resultado.head())

"""output
0      JUAN
1     MARÍA
2    CARLOS
3       ANA
4     PEDRO
Name: nombre, dtype: object
"""
