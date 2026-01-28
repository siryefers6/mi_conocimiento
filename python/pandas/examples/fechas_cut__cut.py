"""
Objetivo: Crear bins de tiempo con cut
Referencia: pd.cut
Tipo: función
Nivel: avanzado
"""

import pandas as pd

# Crear datos de edades
data = {
    'nombre': ['Juan', 'María', 'Carlos', 'Ana', 'Pedro', 'Laura'],
    'edad': [28, 34, 45, 29, 51, 32]
}
df = pd.DataFrame(data)

# Crear categorías de edad
bins = [0, 30, 40, 50, 100]
labels = ['18-30', '30-40', '40-50', '50+']
df['grupo_edad'] = pd.cut(df['edad'], bins=bins, labels=labels, right=False)

print(df)

"""output
    nombre  edad grupo_edad
0    Juan    28       18-30
1   María    34       30-40
2   Carlos    45       40-50
3      Ana    29       18-30
4    Pedro    51         50+
5    Laura    32       30-40
"""
