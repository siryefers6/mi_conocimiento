"""
Objetivo: Eliminar columnas del DataFrame
Referencia: drop
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Eliminar columnas específicas
resultado = df.drop(columns=['email', 'fecha_ingreso'])

print(resultado.head())

"""output
  id     nombre   apellido  edad departamento  salario
0  1      Juan      García    28       Ventas    45000
1  2     María       López    34           IT    65000
2  3    Carlos    Martínez    45      Finanzas    75000
3  4       Ana   Rodríguez    29           IT    62000
4  5     Pedro      Sánchez    51      Dirección    95000
"""
