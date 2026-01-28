"""
Objetivo: Ordenar DataFrame por índice
Referencia: sort_index
Tipo: método
Nivel: basico
"""

import pandas as pd

# Crear DataFrame con índice desordenado
data = {
    'nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Pedro'],
    'edad': [28, 34, 45, 29, 51]
}
df = pd.DataFrame(data, index=[4, 2, 0, 3, 1])

print("DataFrame con índice desordenado:")
print(df)

# Ordenar por índice
resultado = df.sort_index()
print("\nDataFrame ordenado por índice:")
print(resultado)

"""output
DataFrame con índice desordenado:
      nombre  edad
4      Juan    28
2     María    34
0    Carlos    45
3       Ana    29
1     Pedro    51

DataFrame ordenado por índice:
    nombre  edad
0  Carlos    45
1   Pedro    51
2   María    34
3      Ana    29
4     Juan    28
"""
