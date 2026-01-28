"""
Objetivo: Apilar columnas (convierte columnas en índice)
Referencia: stack
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'nombre': ['Juan', 'María'],
    'edad': [28, 34],
    'salario': [45000, 65000]
}
df = pd.DataFrame(data)

# Stack
resultado = df.set_index('nombre').stack()
print(resultado)

"""output