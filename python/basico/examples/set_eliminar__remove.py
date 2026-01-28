"""
Objetivo: Eliminar un elemento de un set
Referencia: remove
Tipo: método
Nivel: basico
"""

# remover elemento
numeros = {1, 2, 3, 4, 5}
print("Original:", numeros)

numeros.remove(3)
print("Después de remove(3):", numeros)

# error si no existe
# numeros.remove(99)  # KeyError

# usar discard (no error)
numeros.discard(99)
print("Con discard:", numeros)

"""output
Original: {1, 2, 3, 4, 5}
Después de remove(3): {1, 2, 4, 5}
Con discard: {1, 2, 4, 5}
"""
