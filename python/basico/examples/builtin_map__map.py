"""
Objetivo: Aplicar función a cada elemento
Referencia: map
Tipo: función
Nivel: basico
"""

# map con función
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# map con función definida
def duplicar(x):
    return x * 2

numeros2 = [10, 20, 30]
duplicados = list(map(duplicar, numeros2))
print(duplicados)

# map con múltiples listas
lista1 = [1, 2, 3]
lista2 = [10, 20, 30]
sumas = list(map(lambda x, y: x + y, lista1, lista2))
print(sumas)

"""output
[1, 4, 9, 16, 25]
[20, 40, 60]
[11, 22, 33]
"""
