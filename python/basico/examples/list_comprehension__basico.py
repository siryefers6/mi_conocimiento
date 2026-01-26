"""
Objetivo: crear una lista aplicando una expresión a cada elemento de otra lista
Referencia: [x for x in ...]
Tipo: sintaxis
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3, 4, 5]

# transformación: obtener cuadrados de cada número
cuadrados = [x**2 for x in numeros]

# resultado
print(cuadrados)

"""output
[1, 4, 9, 16, 25]
"""
