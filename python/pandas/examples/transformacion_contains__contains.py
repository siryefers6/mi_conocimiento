"""
Objetivo: Buscar patrón en string
Referencia: .str.contains
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Buscar emails de ejemplo.com
resultado = df[df['email'].str.contains('example.com')]
print(resultado[['nombre', 'email']])

"""output
      nombre                    email
0      Juan      juan.garcia@example.com
1     María       maria.lopez@example.com
2    Carlos   carlos.martinez@example.com
3       Ana    ana.rodriguez@example.com
4     Pedro    pedro.sanchez@example.com
5     Laura   laura.fernandez@example.com
6    Miguel     miguel.garcia@example.com
7     Isabel      isabel.lopez@example.com
8  Francisco    francisco.ruiz@example.com
9      Elena       elena.diaz@example.com
"""
