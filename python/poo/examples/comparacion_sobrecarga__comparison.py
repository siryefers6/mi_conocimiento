"""
Objetivo: Sobrecargar operadores de comparación
Referencia: __lt__, __le__, __gt__, __ge__
Tipo: método especial
Nivel: basico
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __lt__(self, otro):
        return self.edad < otro.edad
    
    def __le__(self, otro):
        return self.edad <= otro.edad
    
    def __gt__(self, otro):
        return self.edad > otro.edad
    
    def __ge__(self, otro):
        return self.edad >= otro.edad
    
    def __repr__(self):
        return f"{self.nombre}({self.edad})"

p1 = Persona("Ana", 30)
p2 = Persona("Juan", 25)

print(f"p1 > p2: {p1 > p2}")
print(f"p1 < p2: {p1 < p2}")
print(f"p1 >= p2: {p1 >= p2}")

# ordenar
personas = [p1, p2, Persona("Carlos", 28)]
ordenada = sorted(personas)
print(f"Ordenadas: {ordenada}")

"""output
p1 > p2: True
p1 < p2: False
p1 >= p2: True
Ordenadas: [Juan(25), Carlos(28), Ana(30)]
"""
