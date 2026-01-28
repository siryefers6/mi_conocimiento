"""
Objetivo: Obtener valores únicos en una columna
Referencia: unique
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Obtener valores únicos en departamento
resultado = df['departamento'].unique()
print(resultado)

"""output
['Ventas' 'IT' 'Finanzas' 'Dirección' 'Recursos Humanos']
"""
