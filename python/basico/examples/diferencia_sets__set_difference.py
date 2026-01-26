"""
Objetivo: obtener elementos de un set que no están en otro
Referencia: set.difference
Tipo: metodo
Nivel: basico
"""

# carga de datos
a = {1, 2, 3}
b = {2, 3, 4}

# transformación
diferencia = a.difference(b)

# resultado
print(diferencia)

"""output
{1}
"""
