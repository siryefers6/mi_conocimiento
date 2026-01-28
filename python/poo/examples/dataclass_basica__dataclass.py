"""
Objetivo: Usar @dataclass para simplificar clases
Referencia: @dataclass
Tipo: decorador
Nivel: basico
"""

from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    ciudad: str = "Madrid"

p1 = Persona("Ana", 30)
print(f"Persona 1: {p1}")

p2 = Persona("Juan", 25, "Barcelona")
print(f"Persona 2: {p2}")

# Comparación
p3 = Persona("Ana", 30)
print(f"p1 == p3: {p1 == p3}")

"""output
Persona 1: Persona(nombre='Ana', edad=30, ciudad='Madrid')
Persona 2: Persona(nombre='Juan', edad=25, ciudad='Barcelona')
p1 == p3: True
"""
