"""
Objetivo: Eliminar y devolver un elemento de una lista
Referencia: pop
Tipo: método
Nivel: basico
"""

# pop sin índice (último elemento)
numeros = [1, 2, 3, 4, 5]
eliminado = numeros.pop()
print(f"Eliminado: {eliminado}")
print(f"Lista: {numeros}")

# pop con índice
frutas = ["manzana", "plátano", "cereza"]
frutas.pop(1)
print(f"Después de pop(1): {frutas}")

# pop primer elemento
lista = [10, 20, 30]
primero = lista.pop(0)
print(f"Primer eliminado: {primero}, Lista: {lista}")

"""output
Eliminado: 5
Lista: [1, 2, 3, 4]
Después de pop(1): ['manzana', 'cereza']
Primer eliminado: 10, Lista: [20, 30]
"""
