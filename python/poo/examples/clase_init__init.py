"""
Objetivo: Usar constructor para inicializar atributos
Referencia: __init__
Tipo: método especial
Nivel: basico
"""

# clase con constructor
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.saludos = 0

# crear objeto
persona = Persona("Ana", 30)
print(f"Nombre: {persona.nombre}")
print(f"Edad: {persona.edad}")
print(f"Saludos: {persona.saludos}")

# otra persona
persona2 = Persona("Juan", 25)
print(f"{persona2.nombre} tiene {persona2.edad} años")

"""output
Nombre: Ana
Edad: 30
Saludos: 0
Juan tiene 25 años
"""
