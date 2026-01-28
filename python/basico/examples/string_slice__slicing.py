"""
Objetivo: Obtener una porción de una cadena
Referencia: [:]
Tipo: operador
Nivel: basico
"""

# slicing básico
texto = "Hola mundo"
print(texto[0:4])
print(texto[5:10])

# desde inicio o hasta fin
print(texto[:4])
print(texto[5:])

# con pasos
print(texto[::2])
print(texto[::-1])

"""output
Hola
mundo
Hola
 mundo
Hlomno
odnum aloH
"""
