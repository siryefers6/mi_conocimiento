"""
Objetivo: Obtener cantidad de elementos en un set
Referencia: len
Tipo: función
Nivel: basico
"""

# largo de set
numeros = {1, 2, 3, 4, 5}
cantidad = len(numeros)
print(f"Set tiene {cantidad} elementos")

# set vacío
vacio = set()
print(f"Set vacío: {len(vacio)} elementos")

# set de lista
conjunto = set([1, 1, 2, 2, 3])
print(f"De duplicados: {len(conjunto)} elementos")

"""output
Set tiene 5 elementos
Set vacío: 0 elementos
De duplicados: 3 elementos
"""
