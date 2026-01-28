"""
Objetivo: Ver las primeras filas de un DataFrame
Referencia: head
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Ver primeras 3 filas
resultado = df.head(3)
print(resultado)

"""output
  id      nombre   apellido  edad                   email departamento  salario fecha_ingreso
0  1        Juan      García    28   juan.garcia@example.com       Ventas    45000   2021-03-15
1  2       María       López    34    maria.lopez@example.com          IT    65000   2019-07-22
2  3      Carlos    Martínez    45  carlos.martinez@example.com     Finanzas    75000   2018-01-10
"""
