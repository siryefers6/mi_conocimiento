"""
Objetivo: Agregar elemento a un set
Referencia: add
Tipo: método
Nivel: basico
"""

# agregar elemento
numeros = {1, 2, 3}
print("Original:", numeros)

numeros.add(4)
print("Después de add(4):", numeros)

# agregar duplicado (no hace nada)
numeros.add(2)
print("Agregar existente:", numeros)

"""output
Original: {1, 2, 3}
Después de add(4): {1, 2, 3, 4}
Agregar existente: {1, 2, 3, 4}
"""
