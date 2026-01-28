"""
Objetivo: Usar @property para crear propiedades
Referencia: @property
Tipo: decorador
Nivel: basico
"""

class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def radio(self):
        return self._radio
    
    @property
    def area(self):
        return 3.14159 * self._radio ** 2

circulo = Circulo(5)
print(f"Radio: {circulo.radio}")
print(f"Área: {circulo.area:.2f}")

# no se puede asignar sin setter
try:
    circulo.area = 100
except AttributeError as e:
    print(f"Error: No se puede asignar a property")

"""output
Radio: 5
Área: 78.54
Error: No se puede asignar a property
"""
