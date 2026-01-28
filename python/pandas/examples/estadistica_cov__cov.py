"""
Objetivo: Calcular covarianza entre columnas
Referencia: cov
Tipo: método
Nivel: avanzado
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/calificaciones.csv')

# Calcular matriz de covarianza
resultado = df[['matematica', 'fisica', 'historia']].cov()
print("Matriz de covarianza:")
print(resultado)

"""output
Matriz de covarianza:
             matematica    fisica   historia
matematica  108.571429  80.714286  70.571429
fisica       80.714286  74.285714  62.285714
historia     70.571429  62.285714  75.142857
"""
