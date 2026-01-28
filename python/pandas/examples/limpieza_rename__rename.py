"""
Objetivo: Renombrar columnas del DataFrame
Referencia: rename
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Renombrar columnas específicas
resultado = df.rename(columns={
    'nombre': 'Nombre',
    'edad': 'Años',
    'salario': 'Sueldo'
})

print(resultado[['Nombre', 'Años', 'Sueldo']].head())

"""output
   Nombre  Años  Sueldo
0    Juan    28   45000
1   María    34   65000
2  Carlos    45   75000
3     Ana    29   62000
4   Pedro    51   95000
"""
