"""
Objetivo: Reemplazar texto en una columna
Referencia: .str.replace
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Reemplazar dominio en email
resultado = df['email'].str.replace('example.com', 'company.com')
print(resultado.head())

"""output
0     juan.garcia@company.com
1      maria.lopez@company.com
2   carlos.martinez@company.com
3     ana.rodriguez@company.com
4     pedro.sanchez@company.com
Name: email, dtype: object
"""
