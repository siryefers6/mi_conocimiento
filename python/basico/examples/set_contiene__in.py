"""
Objetivo: Verificar si un elemento está en un set
Referencia: in
Tipo: operador
Nivel: basico
"""

# verificar existencia
numeros = {1, 2, 3, 4, 5}
print(3 in numeros)
print(10 in numeros)

# con strings
colores = {"rojo", "verde", "azul"}
print("rojo" in colores)
print("amarillo" in colores)

# negación
print(99 not in numeros)

"""output
True
False
True
False
True
"""
