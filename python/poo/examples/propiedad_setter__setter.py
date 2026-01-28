"""
Objetivo: Usar @setter en propiedades
Referencia: @property.setter
Tipo: decorador
Nivel: basico
"""

class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura imposible")
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperatura(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")

temp.celsius = 0
print(f"Nuevo Celsius: {temp.celsius}")
print(f"Nuevo Fahrenheit: {temp.fahrenheit}")

"""output
Celsius: 25
Fahrenheit: 77.0
Nuevo Celsius: 0
Nuevo Fahrenheit: 32.0
"""
