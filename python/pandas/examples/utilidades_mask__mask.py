"""
Objetivo: Filtrar valores con condición booleana inversa (mask)
Referencia: mask
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

# Reemplazar con NaN donde edad <= 30 (inverso de where)
resultado = df['edad'].mask(df['edad'] <= 30)
print("Edad (reemplazar <= 30 con NaN):")
print(resultado)

# Reemplazar salarios donde edad <= 30 con NaN
resultado_sal = df['salario'].mask(df['edad'] <= 30)
print("\nSalarios (reemplazar si edad <= 30 con NaN):")
print(resultado_sal)

"""output
Edad (reemplazar <= 30 con NaN):
0      NaN
1     34.0
2     45.0
3      NaN
Name: edad, dtype: float64

Salarios (reemplazar si edad <= 30 con NaN):
0         NaN
1    65000.0
2    75000.0
3         NaN
Name: salario, dtype: float64
"""
