"""
Objetivo: Eliminar la primera ocurrencia de un valor
Referencia: remove
Tipo: método
Nivel: basico
"""

# remover por valor
numeros = [1, 2, 3, 2, 4]
numeros.remove(2)
print("Después de remove(2):", numeros)

# remover string
frutas = ["manzana", "plátano", "manzana"]
frutas.remove("manzana")
print("Después de remove('manzana'):", frutas)

# error si no existe
# numeros.remove(99)  # ValueError

"""output
Después de remove(2): [1, 3, 2, 4]
Después de remove('manzana'): ['plátano', 'manzana']
"""
