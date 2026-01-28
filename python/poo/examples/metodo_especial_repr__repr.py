"""
Objetivo: Implementar __repr__ para representación técnica
Referencia: __repr__
Tipo: método especial
Nivel: basico
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

punto = Punto(3, 4)
print(repr(punto))
print(punto)

# para debugging
puntos = [Punto(0, 0), Punto(1, 1), Punto(2, 2)]
print(puntos)

"""output
Punto(3, 4)
Punto(3, 4)
[Punto(0, 0), Punto(1, 1), Punto(2, 2)]
"""
