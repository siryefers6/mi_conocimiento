"""
Objetivo: Aplicar función a cada elemento de una columna o DataFrame
Referencia: apply
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Aplicar función personalizada
def categorizar_edad(edad):
    if edad < 30:
        return 'Joven'
    elif edad < 50:
        return 'Adulto'
    else:
        return 'Senior'

df['categoria_edad'] = df['edad'].apply(categorizar_edad)
print(df[['nombre', 'edad', 'categoria_edad']])

"""output
      nombre  edad categoria_edad
0      Juan    28          Joven
1     María    34         Adulto
2    Carlos    45         Adulto
3       Ana    29          Joven
4     Pedro    51         Senior
5     Laura    32         Adulto
6    Miguel    27          Joven
7     Isabel    38         Adulto
8  Francisco    55         Senior
9      Elena    31         Adulto
"""
