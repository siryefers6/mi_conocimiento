"""
Objetivo: Concatenar DataFrames verticalmente
Referencia: concat
Tipo: función
Nivel: intermedio
"""

import pandas as pd

# Crear datos de ejemplo
df1 = pd.DataFrame({
    'id': [1, 2],
    'nombre': ['Juan', 'María']
})

df2 = pd.DataFrame({
    'id': [3, 4],
    'nombre': ['Carlos', 'Ana']
})

# Concatenar verticalmente
resultado = pd.concat([df1, df2], ignore_index=True)
print(resultado)

"""output
   id     nombre
0   1       Juan
1   2      María
2   3     Carlos
3   4        Ana
"""
