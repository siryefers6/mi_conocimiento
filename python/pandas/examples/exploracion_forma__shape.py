"""
Objetivo: Obtener la forma (filas, columnas) del DataFrame
Referencia: shape
Tipo: atributo
Nivel: basico
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/personas.csv')

# Obtener forma
filas, columnas = df.shape
print(f"Filas: {filas}, Columnas: {columnas}")

"""output
Filas: 10, Columnas: 8
"""
