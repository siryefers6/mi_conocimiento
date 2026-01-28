"""
Objetivo: Renombrar el nombre del índice
Referencia: rename_axis
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Establecer 'id' como índice
df_con_indice = df.set_index('id')

# Renombrar el eje del índice
df_renombrado = df_con_indice.rename_axis('identificador')

print("Índice renombrado:")
print(df_renombrado.head())

"""output
               nombre   apellido  edad                   email departamento  salario fecha_ingreso
identificador
1              Juan      García    28   juan.garcia@example.com       Ventas    45000   2021-03-15
2             María       López    34    maria.lopez@example.com          IT    65000   2019-07-22
3            Carlos    Martínez    45  carlos.martinez@example.com     Finanzas    75000   2018-01-10
4               Ana   Rodríguez    29  ana.rodriguez@example.com          IT    62000   2022-05-18
5             Pedro      Sánchez    51  pedro.sanchez@example.com      Dirección    95000   2015-11-01
"""
