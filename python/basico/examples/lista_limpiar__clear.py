"""
Objetivo: Eliminar todos los elementos de una lista
Referencia: clear
Tipo: método
Nivel: basico
"""

# limpiar lista
numeros = [1, 2, 3, 4, 5]
print("Original:", numeros)

numeros.clear()
print("Después de clear():", numeros)
print("Largo:", len(numeros))

# lista vacía
vacia = ["x", "y", "z"]
vacia.clear()
print("Vacía:", vacia)

"""output
Original: [1, 2, 3, 4, 5]
Después de clear(): []
Largo: 0
Vacía: []
"""
