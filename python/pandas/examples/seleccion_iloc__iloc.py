"""
Objetivo: Seleccionar filas y columnas por posición con iloc
Referencia: iloc
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Seleccionar fila en posición 2, columna en posición 1
resultado1 = df.iloc[2, 1]
print("Elemento:", resultado1)

# Seleccionar filas 1-3, columnas 1-3
resultado2 = df.iloc[1:4, 1:4]
print("\nSubconjunto:")
print(resultado2)

"""output
Elemento: Carlos

Subconjunto:
    nombre   apellido  edad
1    María      López    34
2   Carlos   Martínez    45
3      Ana  Rodríguez    29
"""
