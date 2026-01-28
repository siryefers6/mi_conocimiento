"""
Objetivo: Crear sets de forma concisa
Referencia: {x for x in}
Tipo: expresión
Nivel: basico
"""

# set comprehension simple
pares = {x for x in range(10) if x % 2 == 0}
print(pares)

# remover duplicados de lista
numeros = [1, 2, 2, 3, 3, 3, 4]
unicos = {x for x in numeros}
print(unicos)

# transformar
palabras = ["hola", "mundo", "hola"]
longitudes = {len(p) for p in palabras}
print(longitudes)

"""output
{0, 2, 4, 6, 8}
{1, 2, 3, 4}
{4, 5}
"""
