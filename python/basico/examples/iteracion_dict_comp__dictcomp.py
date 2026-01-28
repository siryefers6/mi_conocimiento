"""
Objetivo: Crear diccionarios de forma concisa
Referencia: {k:v for}
Tipo: expresión
Nivel: basico
"""

# dict comprehension simple
cuadrados = {x: x**2 for x in range(1, 4)}
print(cuadrados)

# desde lista de tuplas
pares = [(1, "uno"), (2, "dos"), (3, "tres")]
diccionario = {clave: valor for clave, valor in pares}
print(diccionario)

# transformar diccionario
numeros = {"a": 1, "b": 2, "c": 3}
duplicados = {k: v*2 for k, v in numeros.items()}
print(duplicados)

"""output
{1: 1, 2: 4, 3: 9}
{1: 'uno', 2: 'dos', 3: 'tres'}
{'a': 2, 'b': 4, 'c': 6}
"""
