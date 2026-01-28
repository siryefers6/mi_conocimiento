"""
Objetivo: Eliminar una clave y devolver su valor
Referencia: pop
Tipo: método
Nivel: basico
"""

# pop devuelve el valor
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
edad = persona.pop("edad")
print(f"Eliminado: {edad}")
print("Diccionario:", persona)

# con valor por defecto si clave no existe
email = persona.pop("email", "no especificado")
print(f"Email: {email}")

"""output
Eliminado: 30
Diccionario: {'nombre': 'Ana', 'ciudad': 'Madrid'}
Email: no especificado
"""
