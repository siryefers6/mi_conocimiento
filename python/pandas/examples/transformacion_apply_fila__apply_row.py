"""
Objetivo: Aplicar función a cada fila del DataFrame
Referencia: apply(axis=1)
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Crear categoría por salario y edad
def categorizar_perfil(fila):
    if fila['salario'] > 70000:
        return 'Alto-Salario'
    elif fila['edad'] > 40:
        return 'Senior-Experiencia'
    else:
        return 'Estándar'

df['perfil'] = df.apply(categorizar_perfil, axis=1)
print(df[['nombre', 'salario', 'edad', 'perfil']])

"""output
      nombre  salario  edad           perfil
0      Juan    45000    28          Estándar
1     María    65000    34          Estándar
2    Carlos    75000    45     Alto-Salario
3       Ana    62000    29          Estándar
4     Pedro    95000    51     Alto-Salario
5     Laura    52000    32          Estándar
6    Miguel    58000    27          Estándar
7     Isabel    48000    38          Estándar
8  Francisco    82000    55     Alto-Salario
9      Elena    50000    31          Estándar
"""
