"""
Objetivo: verificar condición para todos o alguno de los elementos
Referencia: all / any
Tipo: funcion
Nivel: basico
"""

# carga de datos
numeros = [2, 4, 6]

# transformación
todos_pares = all(n % 2 == 0 for n in numeros)
algun_impar = any(n % 2 != 0 for n in numeros)

# resultado
print(todos_pares)
print(algun_impar)

"""output
True
False
"""
