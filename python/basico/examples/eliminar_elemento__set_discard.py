"""
Objetivo: eliminar un elemento del set sin error si no existe
Referencia: set.discard
Tipo: metodo
Nivel: basico
"""

# carga de datos
valores = {1, 2, 3}

# transformación
valores.discard(4)  # no existe, no lanza error
valores.discard(2)  # elimina el 2

# resultado
print(valores)

"""output
{1, 3}
"""
