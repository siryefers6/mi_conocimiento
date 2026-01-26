"""
Objetivo: eliminar un par por clave y retornar su valor
Referencia: dict.pop
Tipo: metodo
Nivel: basico
"""

# carga de datos
usuario = {"nombre": "Ana", "edad": 30}

# transformación
valor = usuario.pop("edad")

# resultado
print(usuario)
print(valor)

"""output
{'nombre': 'Ana'}
30
"""
