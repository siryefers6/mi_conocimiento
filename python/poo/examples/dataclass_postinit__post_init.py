"""
Objetivo: Usar __post_init__ en dataclass
Referencia: __post_init__
Tipo: método especial
Nivel: basico
"""

from dataclasses import dataclass

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int = 1
    
    def __post_init__(self):
        if self.precio < 0:
            raise ValueError("Precio no puede ser negativo")
        self.total = self.precio * self.cantidad

p1 = Producto("Laptop", 1000, 2)
print(f"Producto: {p1.nombre}")
print(f"Total: {p1.total}")

try:
    p2 = Producto("Mouse", -10)
except ValueError as e:
    print(f"Error: {e}")

"""output
Producto: Laptop
Total: 2000
Error: Precio no puede ser negativo
"""
