"""
Objetivo: crear funciones anónimas para operaciones simples
Referencia: lambda
Tipo: keyword
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3, 4, 5]

# transformación: función lambda para elevar al cuadrado
cuadrados = list(map(lambda x: x**2, numeros))

# resultado
print(cuadrados)

"""output
[1, 4, 9, 16, 25]
"""
