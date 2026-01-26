"""
Objetivo: verificar si un set es superconjunto de otro
Referencia: set.issuperset
Tipo: metodo
Nivel: basico
"""

# carga de datos
a = {1, 2, 3}
b = {1, 2}

# transformación
es_super = a.issuperset(b)

# resultado
print(es_super)

"""output
True
"""
