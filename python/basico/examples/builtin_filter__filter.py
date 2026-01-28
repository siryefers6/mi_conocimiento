"""
Objetivo: Filtrar elementos que cumplan condición
Referencia: filter
Tipo: función
Nivel: basico
"""

# filter con función
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares: {pares}")

# filter con función definida
def es_positivo(x):
    return x > 0

numeros2 = [-2, -1, 0, 1, 2]
positivos = list(filter(es_positivo, numeros2))
print(f"Positivos: {positivos}")

"""output
Pares: [2, 4, 6, 8, 10]
Positivos: [1, 2]
"""
