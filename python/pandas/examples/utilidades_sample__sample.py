"""
Objetivo: Seleccionar muestra aleatoria de filas
Referencia: sample
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Seleccionar 3 filas al azar
resultado = df.sample(n=3)
print("Muestra aleatoria de 3 filas:")
print(resultado[['nombre', 'edad', 'salario']])

# Seleccionar el 20% del DataFrame
resultado_pct = df.sample(frac=0.2)
print(f"\nMuestra del 20% ({len(resultado_pct)} filas):")
print(resultado_pct[['nombre', 'edad']])

"""output
Muestra aleatoria de 3 filas:
     nombre  edad  salario
5    Laura    32    52000
8 Francisco    55    82000
0     Juan    28    45000

Muestra del 20% (2 filas):
   nombre  edad
3      Ana    29
6    Miguel    27
"""
