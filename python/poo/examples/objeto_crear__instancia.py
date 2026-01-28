"""
Objetivo: Crear instancias de una clase
Referencia: ()
Tipo: operador
Nivel: basico
"""

# definir clase
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# crear instancias
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

print(f"Coche 1: {coche1.marca} {coche1.modelo}")
print(f"Coche 2: {coche2.marca} {coche2.modelo}")

# diferentes objetos
print(f"¿Son iguales? {coche1 is coche2}")

"""output
Coche 1: Toyota Corolla
Coche 2: Honda Civic
¿Son iguales? False
"""
