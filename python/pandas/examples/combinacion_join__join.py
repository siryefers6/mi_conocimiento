"""
Objetivo: Combinar dos DataFrames por índice
Referencia: join
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos de ejemplo con índice
df1 = pd.DataFrame({
    'nombre': ['Juan', 'María', 'Carlos']
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    'ciudad': ['Madrid', 'Barcelona', 'Valencia']
}, index=[1, 2, 3])

# Join por índice
resultado = df1.join(df2)
print(resultado)

"""output
     nombre       ciudad
1      Juan      Madrid
2     María   Barcelona
3    Carlos     Valencia
"""
