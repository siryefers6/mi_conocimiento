"""
Objetivo: Cambiar tipo de dato de una columna
Referencia: astype
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Ver tipo actual
print("Tipo original de edad:", df['edad'].dtype)

# Convertir a float
df['edad'] = df['edad'].astype(float)
print("Tipo nuevo de edad:", df['edad'].dtype)

# Convertir a string
df['id'] = df['id'].astype(str)
print("Tipo nuevo de id:", df['id'].dtype)

"""output
Tipo original de edad: int64
Tipo nuevo de edad: float64
Tipo nuevo de id: object
"""
