"""
Objetivo: Crear un diccionario vacío
Referencia: {}
Tipo: literal
Nivel: basico
"""

# crear diccionario vacío
vacio = {}
print("Vacío:", vacio)
print("Tipo:", type(vacio))

# crear con datos
persona = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
print("Persona:", persona)

# diccionario anidado
usuarios = {"juan": {"edad": 25, "email": "juan@mail.com"}}
print("Anidado:", usuarios)

"""output
Vacío: {}
Tipo: <class 'dict'>
Persona: {'nombre': 'Ana', 'edad': 30, 'ciudad': 'Madrid'}
Anidado: {'juan': {'edad': 25, 'email': 'juan@mail.com'}}
"""
