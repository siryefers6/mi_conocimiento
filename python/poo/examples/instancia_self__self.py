"""
Objetivo: Usar self para acceder a atributos de instancia
Referencia: self
Tipo: keyword
Nivel: basico
"""

# self representa la instancia
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"Mi nombre ahora es {self.nombre}")

persona = Persona("Carlos")
persona.saludar()
persona.cambiar_nombre("Diego")
persona.saludar()

"""output
Hola, soy Carlos
Mi nombre ahora es Diego
Hola, soy Diego
"""
