"""
Objetivo: Mapear valores de una serie usando diccionario
Referencia: map
Tipo: método
Nivel: basico
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'nombre': ['Juan', 'María', 'Carlos'],
    'nivel': [1, 2, 3]
}
df = pd.DataFrame(data)

# Mapear valores
mapeo = {1: 'Básico', 2: 'Intermedio', 3: 'Avanzado'}
df['nivel_descripcion'] = df['nivel'].map(mapeo)
print(df)

"""output
    nombre  nivel   nivel_descripcion
0    Juan       1             Básico
1   María       2          Intermedio
2  Carlos       3           Avanzado
"""
