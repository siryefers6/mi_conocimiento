"""
Objetivo: Agrupar datos por una o más columnas
Referencia: groupby
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Agrupar por departamento
resultado = df.groupby('departamento')
print("Grupos por departamento:")
for nombre, grupo in resultado:
    print(f"\n{nombre}:")
    print(grupo[['nombre', 'salario']])

"""output
Grupos por departamento:

Dirección:
    nombre  salario
5  Pedro    95000

Finanzas:
   nombre  salario
2 Carlos   75000
8 Francisco   82000

IT:
   nombre  salario
1  María    65000
3    Ana    62000
6  Miguel    58000

Recursos Humanos:
      nombre  salario
7     Isabel    48000

Ventas:
      nombre  salario
0      Juan    45000
5     Laura    52000
9      Elena    50000
"""
