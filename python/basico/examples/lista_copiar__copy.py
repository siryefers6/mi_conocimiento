"""
Objetivo: Crear una copia de una lista
Referencia: copy
Tipo: método
Nivel: basico
"""

# copiar lista
original = [1, 2, 3]
copia = original.copy()

print("Original:", original)
print("Copia:", copia)

# modificar copia no afecta original
copia[0] = 99
print("Después de modificar copia:")
print("Original:", original)
print("Copia:", copia)

# asignación vs copia
lista1 = [1, 2, 3]
lista2 = lista1  # referencia
lista2[0] = 99
print("Con referencia - lista1:", lista1)

"""output
Original: [1, 2, 3]
Copia: [1, 2, 3]
Después de modificar copia:
Original: [1, 2, 3]
Copia: [99, 2, 3]
Con referencia - lista1: [99, 2, 3]
"""
