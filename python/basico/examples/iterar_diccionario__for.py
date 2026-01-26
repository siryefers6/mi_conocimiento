"""
Objetivo: iterar sobre claves y valores de un diccionario
Referencia: for
Tipo: keyword
Nivel: basico
"""

# imports
# no aplica

# carga de datos
usuario = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Madrid"
}

# transformación
for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

# resultado
# print dentro del bucle produce la salida

"""output
nombre: Ana
edad: 30
ciudad: Madrid
"""
