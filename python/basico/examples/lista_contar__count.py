"""
Objetivo: Contar cuántas veces aparece un valor en una lista
Referencia: count
Tipo: método
Nivel: basico
"""

# contar ocurrencias
numeros = [1, 2, 2, 3, 2, 4]
cantidad = numeros.count(2)
print(f"El número 2 aparece {cantidad} veces")

# contar strings
palabras = ["gato", "perro", "gato", "gato"]
print(f"'gato' aparece {palabras.count('gato')} veces")
print(f"'perro' aparece {palabras.count('perro')} veces")
print(f"'pájaro' aparece {palabras.count('pájaro')} veces")

"""output
El número 2 aparece 3 veces
'gato' aparece 3 veces
'perro' aparece 1 veces
'pájaro' aparece 0 veces
"""
