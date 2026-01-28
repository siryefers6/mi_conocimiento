"""
Objetivo: Obtener elementos comunes entre sets
Referencia: intersection
Tipo: método
Nivel: basico
"""

# intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}

resultado = set1.intersection(set2)
print("Intersección:", resultado)

# también con operador &
resultado2 = set1 & set2
print("Con &:", resultado2)

"""output
Intersección: {2, 3}
Con &: {2, 3}
"""
