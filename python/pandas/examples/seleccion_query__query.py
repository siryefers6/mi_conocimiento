"""
Objetivo: Filtrar DataFrame con expresión query
Referencia: query
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Filtrar con query: edad > 30 AND salario > 50000
resultado = df.query('edad > 30 and salario > 50000')
print(resultado[['nombre', 'edad', 'salario']])

"""output
     nombre  edad  salario
1     María    34    65000
2    Carlos    45    75000
8 Francisco    55    82000
"""
