"""
Objetivo: Crear listas de forma concisa con list comprehension
Referencia: [x for x in]
Tipo: expresión
Nivel: basico
"""

# list comprehension simple
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

# con strings
letras = [letra.upper() for letra in "hola"]
print(letras)

# a partir de lista existente
numeros = [1, 2, 3, 4, 5]
multiplicados = [x * 2 for x in numeros]
print(multiplicados)

"""output
[0, 1, 4, 9, 16]
['H', 'O', 'L', 'A']
[2, 4, 6, 8, 10]
"""
