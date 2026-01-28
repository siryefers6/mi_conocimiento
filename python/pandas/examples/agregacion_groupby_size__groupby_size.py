"""
Objetivo: Contar elementos en cada grupo
Referencia: groupby().size
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Contar personas por departamento
resultado = df.groupby('departamento').size()
print(resultado)

"""output
departamento
Dirección              1
Finanzas               2
IT                     3
Recursos Humanos       1
Ventas                 3
dtype: int64
"""
