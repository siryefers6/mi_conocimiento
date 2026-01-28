"""
Objetivo: Implementar __eq__ para comparación
Referencia: __eq__
Tipo: método especial
Nivel: basico
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __eq__(self, otro):
        if not isinstance(otro, Persona):
            return False
        return self.nombre == otro.nombre and self.edad == otro.edad

p1 = Persona("Ana", 30)
p2 = Persona("Ana", 30)
p3 = Persona("Juan", 25)

print(f"p1 == p2: {p1 == p2}")
print(f"p1 is p2: {p1 is p2}")
print(f"p1 == p3: {p1 == p3}")

"""output
p1 == p2: True
p1 is p2: False
p1 == p3: False
"""
