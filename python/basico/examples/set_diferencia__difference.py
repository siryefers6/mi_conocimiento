"""
Objetivo: Obtener elementos únicos entre sets
Referencia: difference
Tipo: método
Nivel: basico
"""

# difference
set1 = {1, 2, 3}
set2 = {2, 3, 4}

resultado = set1.difference(set2)
print("Diferencia:", resultado)

# también con operador -
resultado2 = set1 - set2
print("Con -:", resultado2)

"""output
Diferencia: {1}
Con -: {1}
"""
