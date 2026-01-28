"""
Objetivo: Implementar __str__ para representación legible
Referencia: __str__
Tipo: método especial
Nivel: basico
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

persona = Persona("Carlos", 30)
print(persona)
print(str(persona))

"""output
Carlos (30 años)
Carlos (30 años)
"""
