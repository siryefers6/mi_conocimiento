"""
Objetivo: Agregar un elemento al final de una lista
Referencia: append
Tipo: método
Nivel: basico
"""

# agregar elemento
numeros = [1, 2, 3]
print("Original:", numeros)

numeros.append(4)
print("Después de append(4):", numeros)

# agregar múltiples
numeros.append(5)
numeros.append(6)
print("Después de agregar más:", numeros)

# agregar lista (como elemento)
frutas = ["manzana"]
frutas.append("plátano")
print("Frutas:", frutas)

"""output
Original: [1, 2, 3]
Después de append(4): [1, 2, 3, 4]
Después de agregar más: [1, 2, 3, 4, 5, 6]
Frutas: ['manzana', 'plátano']
"""
