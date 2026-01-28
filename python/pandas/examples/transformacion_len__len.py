"""
Objetivo: Obtener longitud de string en una columna
Referencia: .str.len
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Obtener longitud
resultado = df['nombre'].str.len()
print(resultado.head())

"""output
0    4
1    5
2    6
3    3
4    5
Name: nombre, dtype: int64
"""
