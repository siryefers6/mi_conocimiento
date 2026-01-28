"""
Objetivo: Verificar si una clave existe en un diccionario
Referencia: in
Tipo: operador
Nivel: basico
"""

# verificar clave
persona = {"nombre": "Ana", "edad": 30}
print("¿'nombre' existe?", "nombre" in persona)
print("¿'email' existe?", "email" in persona)

# uso en condicional
if "edad" in persona:
    print(f"La edad es {persona['edad']}")

# negación
print("¿'ciudad' no existe?", "ciudad" not in persona)

"""output
¿'nombre' existe? True
¿'email' existe? False
La edad es 30
¿'ciudad' no existe? True
"""
