"""
Objetivo: Acceder a un valor específico por posición
Referencia: iat
Tipo: método
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Acceder a valor en fila 3, columna 1 (nombre)
resultado = df.iat[3, 1]
print(resultado)

"""output
Ana
"""
