"""
Objetivo: Acceder a valores por su clave
Referencia: []
Tipo: operador
Nivel: basico
"""

# acceder a valores
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# cambiar valor
persona["edad"] = 31
print("Edad actualizada:", persona["edad"])

# error si clave no existe
# print(persona["email"])  # KeyError

"""output
Nombre: Ana
Edad: 30
Edad actualizada: 31
"""
