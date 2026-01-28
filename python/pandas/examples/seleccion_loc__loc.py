"""
Objetivo: Seleccionar filas y columnas por etiqueta con loc
Referencia: loc
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Seleccionar fila 2 y columna 'nombre'
resultado1 = df.loc[2, 'nombre']
print("Elemento:", resultado1)

# Seleccionar filas 1-3, columnas 'nombre' y 'edad'
resultado2 = df.loc[1:3, ['nombre', 'edad']]
print("\nSubconjunto:")
print(resultado2)

"""output
Elemento: Carlos

Subconjunto:
   nombre  edad
1   María    34
2  Carlos    45
3     Ana    29
"""
