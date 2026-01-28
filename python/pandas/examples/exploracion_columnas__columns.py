"""
Objetivo: Obtener los nombres de las columnas
Referencia: columns
Tipo: atributo
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Obtener nombres de columnas
resultado = df.columns.tolist()
print(resultado)

"""output
['id', 'nombre', 'apellido', 'edad', 'email', 'departamento', 'salario', 'fecha_ingreso']
"""
