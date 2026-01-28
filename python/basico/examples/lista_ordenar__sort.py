"""
Objetivo: Ordenar los elementos de una lista
Referencia: sort
Tipo: método
Nivel: basico
"""

# ordenar números ascendente
numeros = [3, 1, 4, 1, 5, 9]
numeros.sort()
print("Ascendente:", numeros)

# ordenar descendente
numeros2 = [3, 1, 4, 1, 5]
numeros2.sort(reverse=True)
print("Descendente:", numeros2)

# ordenar strings
palabras = ["zebra", "apple", "mango"]
palabras.sort()
print("Palabras:", palabras)

"""output
Ascendente: [1, 1, 3, 4, 5, 9]
Descendente: [5, 4, 3, 1, 1]
Palabras: ['apple', 'mango', 'zebra']
"""
