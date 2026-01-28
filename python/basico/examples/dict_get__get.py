"""
Objetivo: Acceder a valores de forma segura con get()
Referencia: get
Tipo: método
Nivel: basico
"""

# usar get (devuelve None si no existe)
persona = {"nombre": "Ana", "edad": 30}
print("Email:", persona.get("email"))

# con valor por defecto
print("Email:", persona.get("email", "no especificado"))
print("Nombre:", persona.get("nombre", "desconocido"))

# comparar con indexación
# print(persona["email"])  # Error
print(persona.get("email", "No existe"))  # Seguro

"""output
Email: None
Email: no especificado
Nombre: Ana
No existe
"""
