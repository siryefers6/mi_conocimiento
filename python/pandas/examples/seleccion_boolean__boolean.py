"""
Objetivo: Filtrar DataFrame con condición booleana
Referencia: []
Tipo: operador
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Filtrar personas con edad > 30
resultado = df[df['edad'] > 30]
print(resultado[['nombre', 'edad', 'departamento']])

"""output
     nombre  edad departamento
1     María    34           IT
2    Carlos    45      Finanzas
7    Isabel    38  Recursos Humanos
8 Francisco    55      Finanzas
9     Elena    31        Ventas
"""
