"""
Objetivo: eliminar un elemento por índice y retornarlo
Referencia: list.pop
Tipo: metodo
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3]

# transformación
eliminado = numeros.pop(1)  # elimina el elemento en índice 1

# resultado
print(numeros)
print(eliminado)

"""output
[1, 3]
2
"""
