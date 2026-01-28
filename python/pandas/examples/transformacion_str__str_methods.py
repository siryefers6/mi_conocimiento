"""
Objetivo: Acceder a métodos de string en una columna
Referencia: .str
Tipo: accessor
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Usar métodos string
print("Longitud de nombre:")
print(df['nombre'].str.len().head())

print("\nNombre en mayúsculas:")
print(df['nombre'].str.upper().head())

"""output
Longitud de nombre:
0    4
1    5
2    6
3    3
4    5
Name: nombre, dtype: int64

Nombre en mayúsculas:
0      JUAN
1     MARÍA
2    CARLOS
3       ANA
4     PEDRO
Name: nombre, dtype: object
"""
