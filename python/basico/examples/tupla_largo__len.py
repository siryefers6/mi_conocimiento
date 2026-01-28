"""
Objetivo: Obtener el número de elementos en una tupla
Referencia: len
Tipo: función
Nivel: basico
"""

# largo de tupla
frutas = ("manzana", "plátano", "cereza")
cantidad = len(frutas)
print(f"La tupla tiene {cantidad} elementos")

# tupla vacía
vacia = ()
print(f"Tupla vacía: {len(vacia)} elementos")

# tupla grande
numeros = tuple(range(1, 101))
print(f"Números del 1 al 100: {len(numeros)} elementos")

"""output
La tupla tiene 3 elementos
Tupla vacía: 0 elementos
Números del 1 al 100: 100 elementos
"""
