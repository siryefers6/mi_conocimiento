"""
Objetivo: Filtrar elementos mientras se crea una lista
Referencia: [x for x if]
Tipo: expresión
Nivel: basico
"""

# filtrar pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# filtrar strings
palabras = ["hola", "a", "mundo", "python"]
largas = [p for p in palabras if len(p) > 2]
print(largas)

# transformar y filtrar
valores = [1, 2, 3, 4, 5]
resultado = [x*2 for x in valores if x > 2]
print(resultado)

"""output
[2, 4, 6, 8, 10]
['hola', 'mundo', 'python']
[6, 8, 10]
"""
