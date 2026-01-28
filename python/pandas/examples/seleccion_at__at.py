"""
Objetivo: Acceder a un valor específico por etiqueta
Referencia: at
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Acceder a valor en fila 3, columna 'nombre'
resultado = df.at[3, 'nombre']
print(resultado)

"""output
Ana
"""
