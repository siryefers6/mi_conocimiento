"""
Objetivo: Implementar herencia básica
Referencia: class Hija(Padre)
Tipo: keyword
Nivel: basico
"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} ladra: ¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} maúlla: ¡Miau!"

perro = Perro("Rex")
print(perro.hacer_sonido())

gato = Gato("Michi")
print(gato.hacer_sonido())

"""output
Rex ladra: ¡Guau!
Michi maúlla: ¡Miau!
"""
