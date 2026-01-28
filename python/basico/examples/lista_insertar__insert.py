"""
Objetivo: Insertar un elemento en una posición específica
Referencia: insert
Tipo: método
Nivel: basico
"""

# insertar en posición
numeros = [1, 2, 4, 5]
print("Original:", numeros)

numeros.insert(2, 3)
print("Después de insert(2, 3):", numeros)

# insertar al inicio
numeros.insert(0, 0)
print("Insertar al inicio:", numeros)

# insertar al final
numeros.insert(len(numeros), 6)
print("Insertar al final:", numeros)

"""output
Original: [1, 2, 4, 5]
Después de insert(2, 3): [1, 2, 3, 4, 5]
Insertar al inicio: [0, 1, 2, 3, 4, 5]
Insertar al final: [0, 1, 2, 3, 4, 5, 6]
"""
