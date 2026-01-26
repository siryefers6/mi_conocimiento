"""
Objetivo: crear listas usando comprensión con condición y aplicar lambda a cada elemento
Referencia: [x for x in ... if ...], lambda
Tipo: sintaxis/keyword
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3, 4, 5, 6]

# transformación: obtener cuadrados de números pares solo
cuadrados_pares = [(lambda x: x**2)(x) for x in numeros if x % 2 == 0]

# resultado
print(cuadrados_pares)

"""output
[4, 16, 36]
"""
