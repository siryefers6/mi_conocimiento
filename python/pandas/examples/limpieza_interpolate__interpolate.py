"""
Objetivo: Interpolar valores nulos
Referencia: interpolate
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos con valores faltantes ordenados
data = {
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'temperatura': [10.0, None, None, 13.0, 15.0]
}
df = pd.DataFrame(data)

# Interpolar valores nulos
resultado = df['temperatura'].interpolate()
print(resultado)

"""output
0    10.0
1    11.0
2    12.0
3    13.0
4    15.0
Name: temperatura, dtype: float64
"""
