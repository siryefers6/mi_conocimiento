"""
Objetivo: Obtener la unión de dos sets
Referencia: union
Tipo: método
Nivel: basico
"""

# union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

resultado = set1.union(set2)
print("Union:", resultado)

# también con operador |
resultado2 = set1 | set2
print("Con |:", resultado2)

"""output
Union: {1, 2, 3, 4, 5}
Con |: {1, 2, 3, 4, 5}
"""
