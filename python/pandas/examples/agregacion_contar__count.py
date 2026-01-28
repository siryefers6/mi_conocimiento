"""
Objetivo: Contar valores no-nulos en una columna
Referencia: count
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos con faltantes
df = pd.read_csv('../datasets/frutas.csv')

# Contar valores no nulos
resultado = df['cantidad'].count()
print(f"Cantidad no-nulos: {resultado}")

# Contar por columna
resultado_todas = df.count()
print("\nConteo por columna:")
print(resultado_todas)

"""output
Cantidad no-nulos: 8

Conteo por columna:
id          10
producto    10
cantidad     8
precio       9
fecha       10
dtype: int64
"""
