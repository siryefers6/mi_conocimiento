"""
Objetivo: Dividir string por delimitador
Referencia: .str.split
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Dividir email por '@'
resultado = df['email'].str.split('@', expand=True)
resultado.columns = ['usuario', 'dominio']
print(resultado.head())

"""output
     usuario         dominio
0   juan.garcia   example.com
1    maria.lopez   example.com
2 carlos.martinez   example.com
3   ana.rodriguez   example.com
4   pedro.sanchez   example.com
"""
