"""
Objetivo: Sobrecargar operadores
Referencia: __add__, __sub__, __mul__, etc
Tipo: método especial
Nivel: basico
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)
    
    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)

print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2 = {v1 * 2}")

"""output
v1 + v2 = Vector(3, 7)
v1 - v2 = Vector(1, -1)
v1 * 2 = Vector(4, 6)
"""
