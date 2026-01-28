"""
Objetivo: Filtrar filas donde una columna contiene valores en una lista
Referencia: isin
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Filtrar personas de departamentos específicos
departamentos = ['IT', 'Ventas']
resultado = df[df['departamento'].isin(departamentos)]
print("Personas en IT o Ventas:")
print(resultado[['nombre', 'departamento']])

# Filtrar por IDs específicos
ids = [1, 3, 5]
resultado_ids = df[df['id'].isin(ids)]
print("\nPersonas con ID 1, 3 o 5:")
print(resultado_ids[['id', 'nombre']])

"""output
Personas en IT o Ventas:
      nombre departamento
0       Juan       Ventas
1      María           IT
3        Ana           IT
5      Laura       Ventas
6     Miguel           IT

Personas con ID 1, 3 o 5:
  id   nombre
0  1     Juan
2  3    Carlos
4  5    Pedro
"""
