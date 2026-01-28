"""
Objetivo: Obtener una porción de una tupla
Referencia: [:]
Tipo: operador
Nivel: basico
"""

# slicing
tupla = (0, 1, 2, 3, 4, 5)
print("Índices 1:4:", tupla[1:4])
print("Primeros 3:", tupla[:3])
print("Últimos 2:", tupla[-2:])

# con pasos
print("Índices pares:", tupla[::2])
print("Invertida:", tupla[::-1])

"""output
Índices 1:4: (1, 2, 3)
Primeros 3: (0, 1, 2)
Últimos 2: (4, 5)
Índices pares: (0, 2, 4)
Invertida: (5, 4, 3, 2, 1, 0)
"""
