"""
Objetivo: Implementar composición
Referencia: composición
Tipo: patrón
Nivel: basico
"""

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
    
    def arrancar(self):
        return f"Motor de {self.potencia}HP arrancando"

class Coche:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor
    
    def comenzar_viaje(self):
        print(self.motor.arrancar())
        print(f"{self.marca} en movimiento")

motor = Motor(150)
coche = Coche("Toyota", motor)
coche.comenzar_viaje()

"""output
Motor de 150HP arrancando
Toyota en movimiento
"""
