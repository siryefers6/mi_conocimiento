"""
Objetivo: filtrar elementos según condición
Referencia: filter
Tipo: funcion
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3, 4, 5]

# transformación
pares = list(filter(lambda x: x % 2 == 0, numeros))

# resultado
print(pares)

"""output
[2, 4]
"""
