"""
Objetivo: aplicar una función a todos los elementos de una secuencia
Referencia: map
Tipo: funcion
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3, 4]

# transformación
cuadrados = list(map(lambda x: x**2, numeros))

# resultado
print(cuadrados)

"""output
[1, 4, 9, 16]
"""
