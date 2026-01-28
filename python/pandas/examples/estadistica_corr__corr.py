"""
Objetivo: Calcular correlación entre columnas
Referencia: corr
Tipo: método
Nivel: avanzado
"""

import pandas as pd

# Cargar datos
df = pd.read_csv('../datasets/calificaciones.csv')

# Calcular matriz de correlación
resultado = df[['matematica', 'fisica', 'historia', 'inglés']].corr()
print("Matriz de correlación:")
print(resultado)

# Correlación con una columna específica
corr_math = df['matematica'].corr(df['fisica'])
print(f"\nCorrelación Matemática-Física: {corr_math:.3f}")

"""output
Matriz de correlación:
             matematica    fisica   historia    inglés
matematica      1.000000  0.893066   0.804626  0.862721
fisica          0.893066  1.000000   0.829319  0.897127
historia        0.804626  0.829319   1.000000  0.887813
inglés          0.862721  0.897127   0.887813  1.000000

Correlación Matemática-Física: 0.893
"""
