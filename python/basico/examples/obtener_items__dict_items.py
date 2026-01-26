"""
Objetivo: obtener pares clave-valor del diccionario
Referencia: dict.items
Tipo: metodo
Nivel: basico
"""

# carga de datos
usuario = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

# transformación
items = usuario.items()

# resultado
print(items)

"""output
dict_items([('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Madrid')])
"""
