"""
Objetivo: Ver las últimas filas de un DataFrame
Referencia: tail
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Ver últimas 2 filas
resultado = df.tail(2)
print(resultado)

"""output
   id      nombre   apellido  edad                   email departamento  salario fecha_ingreso
8   9   Francisco       Ruiz    55  francisco.ruiz@example.com     Finanzas    82000   2016-08-20
9  10      Elena       Díaz    31    elena.diaz@example.com       Ventas    50000   2021-12-08
"""
