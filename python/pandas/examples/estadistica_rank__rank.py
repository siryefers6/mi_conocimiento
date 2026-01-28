"""
Objetivo: Calcular ranking/ordenamiento de valores
Referencia: rank
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Ranking de salarios
df['rank_salario'] = df['salario'].rank(ascending=False)

# Mostrar resultado
resultado = df[['nombre', 'salario', 'rank_salario']].sort_values('rank_salario')
print(resultado)

"""output
       nombre  salario  rank_salario
4      Pedro    95000           1.0
8   Francisco    82000           2.0
2     Carlos    75000           3.0
1      María    65000           4.0
6     Miguel    58000           5.0
5      Laura    52000           6.0
9      Elena    50000           7.0
7      Isabel    48000           8.0
0       Juan    45000           9.0
3        Ana    62000          10.0
"""
