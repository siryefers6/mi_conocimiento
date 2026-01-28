"""
Objetivo: Contar frecuencia de valores en una columna
Referencia: value_counts
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Contar valores únicos
resultado = df['departamento'].value_counts()
print(resultado)

"""output
departamento
Ventas               3
IT                   2
Finanzas             2
Recursos Humanos     1
Dirección            1
Name: count, dtype: int64
"""
