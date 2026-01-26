"""
Objetivo: agregar varios elementos al final de la lista
Referencia: list.extend
Tipo: metodo
Nivel: basico
"""

# carga de datos
numeros = [1, 2]
otros = [3, 4]

# transformación
numeros.extend(otros)

# resultado
print(numeros)

"""output
[1, 2, 3, 4]
"""
