"""
Objetivo: Remodelar datos (similar a pivot_table sin agregación)
Referencia: pivot
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'id': [1, 1, 2, 2],
    'asignatura': ['Matemáticas', 'Historia', 'Matemáticas', 'Historia'],
    'calificacion': [95, 88, 78, 85]
}
df = pd.DataFrame(data)

# Pivotar
resultado = df.pivot(index='id', columns='asignatura', values='calificacion')
print(resultado)

"""output
asignatura  Historia  Matemáticas
id                                
1                 88            95
2                 85            78
"""
