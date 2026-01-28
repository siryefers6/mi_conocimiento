"""
Objetivo: Obtener el número de elementos en una lista
Referencia: len
Tipo: función
Nivel: basico
"""

# largo de lista
frutas = ["manzana", "plátano", "cereza"]
cantidad = len(frutas)
print(f"La lista tiene {cantidad} elementos")

# lista vacía
vacia = []
print(f"Lista vacía: {len(vacia)} elementos")

# lista grande
numeros = list(range(1, 101))
print(f"Números del 1 al 100: {len(numeros)} elementos")

"""output
La lista tiene 3 elementos
Lista vacía: 0 elementos
Números del 1 al 100: 100 elementos
"""
