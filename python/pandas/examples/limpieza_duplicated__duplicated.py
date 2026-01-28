"""
Objetivo: Detectar filas duplicadas
Referencia: duplicated
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

# Detectar duplicados (mantiene primer registro como no duplicado)
resultado = df.duplicated()
print(resultado)

"""output
0    False
1    False
2     True
3    False
4     True
dtype: bool
"""
