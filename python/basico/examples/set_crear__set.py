"""
Objetivo: Crear un conjunto vacío
Referencia: set
Tipo: función
Nivel: basico
"""

# crear set vacío (usar set())
vacio = set()
print("Set vacío:", vacio)
print("Tipo:", type(vacio))

# crear set con elementos
numeros = {1, 2, 3, 4, 5}
print("Números:", numeros)

# set automáticamente quita duplicados
datos = {1, 2, 2, 3, 3, 3}
print("Sin duplicados:", datos)

# set a partir de lista
lista = [1, 2, 2, 3, 3]
conjunto = set(lista)
print("De lista:", conjunto)

"""output
Set vacío: set()
Tipo: <class 'set'>
Números: {1, 2, 3, 4, 5}
Sin duplicados: {1, 2, 3}
De lista: {1, 2, 3}
"""
