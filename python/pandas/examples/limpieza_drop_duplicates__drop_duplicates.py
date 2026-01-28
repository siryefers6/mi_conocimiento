"""
Objetivo: Eliminar filas duplicadas
Referencia: drop_duplicates
Tipo: método
Nivel: basico
"""

import pandas as pd

# Crear datos con duplicados
data = {
    'nombre': ['Juan', 'María', 'Juan', 'Carlos', 'María'],
    'edad': [28, 34, 28, 45, 34]
}
df = pd.DataFrame(data)

# Eliminar duplicados
resultado = df.drop_duplicates()
print(resultado)

"""output
  nombre  edad
0   Juan    28
1  María    34
3 Carlos    45
"""
