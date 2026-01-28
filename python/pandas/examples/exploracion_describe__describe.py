"""
Objetivo: Obtener estadísticas descriptivas del DataFrame
Referencia: describe
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Estadísticas básicas
resultado = df.describe()
print(resultado)

"""output
        id       edad   salario
count  10.0      10.0      10.0
mean    5.5      35.9   61600.0
std     3.162278  10.449915  16097.282889
min     1.0      27.0    45000.0
25%     3.25     29.75   48500.0
50%     5.5      33.0    58000.0
75%     7.75     42.5    72250.0
max    10.0      55.0    95000.0
"""
