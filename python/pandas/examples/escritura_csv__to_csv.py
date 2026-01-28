"""
Objetivo: Guardar DataFrame en archivo CSV
Referencia: to_csv
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Guardar en CSV sin índice
df.to_csv('personas_guardado.csv', index=False)

# Leer de vuelta para verificar
resultado = pd.read_csv('personas_guardado.csv')
print(resultado.head())

"""output
  id         nombre    apellido  edad                   email departamento  salario fecha_ingreso
0  1           Juan       García    28   juan.garcia@example.com       Ventas    45000   2021-03-15
1  2          María        López    34    maria.lopez@example.com          IT    65000   2019-07-22
2  3         Carlos     Martínez    45  carlos.martinez@example.com     Finanzas    75000   2018-01-10
3  4            Ana    Rodríguez    29  ana.rodriguez@example.com          IT    62000   2022-05-18
4  5          Pedro       Sánchez    51  pedro.sanchez@example.com      Dirección    95000   2015-11-01
"""
