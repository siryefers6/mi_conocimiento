"""
Objetivo: Contar ocurrencias de un valor en una tupla
Referencia: count
Tipo: método
Nivel: basico
"""

# contar ocurrencias
numeros = (1, 2, 2, 3, 2, 4)
cantidad = numeros.count(2)
print(f"El número 2 aparece {cantidad} veces")

# con strings
palabras = ("gato", "perro", "gato")
print(f"'gato' aparece {palabras.count('gato')} veces")

# no existe
print(f"'pájaro' aparece {palabras.count('pájaro')} veces")

"""output
El número 2 aparece 3 veces
'gato' aparece 2 veces
'pájaro' aparece 0 veces
"""
