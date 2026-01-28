"""
Objetivo: Filtrar valores con condición booleana (where)
Referencia: where
Tipo: método
Nivel: intermedio
"""

import pandas as pd

# Crear datos de ejemplo
data = {
    'nombre': ['Juan', 'María', 'Carlos', 'Ana'],
    'edad': [28, 34, 45, 29],
    'salario': [45000, 65000, 75000, 62000]
}
df = pd.DataFrame(data)

# Mantener solo valores donde edad > 30, reemplazar otros con NaN
resultado = df['edad'].where(df['edad'] > 30)
print("Edad (solo > 30):")
print(resultado)

# Mantener solo salarios donde edad > 30
resultado_sal = df['salario'].where(df['edad'] > 30)
print("\nSalarios (solo si edad > 30):")
print(resultado_sal)

"""output
Edad (solo > 30):
0      NaN
1     34.0
2     45.0
3     29.0
Name: edad, dtype: float64

Salarios (solo si edad > 30):
0         NaN
1    65000.0
2    75000.0
3         NaN
Name: salario, dtype: float64
"""
