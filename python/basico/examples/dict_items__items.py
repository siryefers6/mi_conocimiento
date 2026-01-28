"""
Objetivo: Obtener pares clave-valor como tuplas
Referencia: items
Tipo: método
Nivel: basico
"""

# obtener items
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
items = persona.items()
print("Items:", items)

# iterar sobre items
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

"""output
Items: dict_items([('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Madrid')])
nombre: Ana
edad: 30
ciudad: Madrid
"""
