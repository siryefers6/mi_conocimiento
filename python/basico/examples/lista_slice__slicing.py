"""
Objetivo: Obtener una porción de una lista
Referencia: [:]
Tipo: operador
Nivel: basico
"""

# slicing básico
lista = [0, 1, 2, 3, 4, 5]
print("Índices 1:4:", lista[1:4])
print("Primeros 3:", lista[:3])
print("Últimos 2:", lista[-2:])

# con pasos
print("Índices pares:", lista[::2])
print("Invertida:", lista[::-1])

# modificar con slicing
numeros = [1, 2, 3, 4, 5]
numeros[1:3] = [20, 30]
print("Modificada:", numeros)

"""output
Índices 1:4: [1, 2, 3]
Primeros 3: [0, 1, 2]
Últimos 2: [4, 5]
Índices pares: [0, 2, 4]
Invertida: [5, 4, 3, 2, 1, 0]
Modificada: [1, 20, 30, 4, 5]
"""
