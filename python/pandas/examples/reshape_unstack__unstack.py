"""
Objetivo: Desapilar índice (inverso de stack)
Referencia: unstack
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos apilados
data = {
    'nombre': ['Juan', 'Juan', 'María', 'María'],
    'tipo': ['edad', 'salario', 'edad', 'salario'],
    'valor': [28, 45000, 34, 65000]
}
df = pd.DataFrame(data)
df_stacked = df.set_index(['nombre', 'tipo'])['valor']

# Unstack
resultado = df_stacked.unstack()
print(resultado)

"""output
tipo    edad   salario
nombre                
Juan      28     45000
María     34     65000
"""
