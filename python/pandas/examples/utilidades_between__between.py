"""
Objetivo: Filtrar valores dentro de un rango
Referencia: between
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Filtrar personas con edad entre 30 y 45
resultado = df[df['edad'].between(30, 45)]
print("Personas con edad entre 30 y 45:")
print(resultado[['nombre', 'edad']])

# Filtrar salarios entre 50000 y 70000
resultado_sal = df[df['salario'].between(50000, 70000)]
print("\nPersonas con salario entre 50000 y 70000:")
print(resultado_sal[['nombre', 'salario']])

"""output
Personas con edad entre 30 y 45:
      nombre  edad
1     María    34
2    Carlos    45
5    Laura    32
7    Isabel    38
9     Elena    31

Personas con salario entre 50000 y 70000:
    nombre  salario
1   María    65000
3      Ana    62000
5   Laura    52000
"""
