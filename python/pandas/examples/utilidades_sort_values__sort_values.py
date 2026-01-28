"""
Objetivo: Ordenar DataFrame por valores de columna
Referencia: sort_values
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Ordenar por edad ascendente
resultado_asc = df.sort_values('edad')[['nombre', 'edad']].head()
print("Ordenado por edad (ascendente):")
print(resultado_asc)

# Ordenar por salario descendente
resultado_desc = df.sort_values('salario', ascending=False)[['nombre', 'salario']].head()
print("\nOrdenado por salario (descendente):")
print(resultado_desc)

"""output
Ordenado por edad (ascendente):
     nombre  edad
6    Miguel    27
0     Juan    28
3      Ana    29
5    Laura    32
9     Elena    31

Ordenado por salario (descendente):
       nombre  salario
4      Pedro    95000
8   Francisco    82000
2     Carlos    75000
1      María    65000
3        Ana    62000
"""
