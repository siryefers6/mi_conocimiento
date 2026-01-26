"""
Objetivo: agregar o modificar pares en un diccionario
Referencia: dict.update
Tipo: metodo
Nivel: basico
"""

# carga de datos
usuario = {"nombre": "Ana", "edad": 30}

# transformación
usuario.update({"edad": 31, "ciudad": "Madrid"})

# resultado
print(usuario)

"""output
{'nombre': 'Ana', 'edad': 31, 'ciudad': 'Madrid'}
"""
