"""
Objetivo: Crear clases abstractas con ABC
Referencia: ABC, abstractmethod
Tipo: módulo/decorador
Nivel: basico
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass
    
    def dormir(self):
        return "Zzz..."

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

# no puedo instanciar Animal
# animal = Animal()  # Error

perro = Perro()
print(perro.hacer_sonido())
print(perro.dormir())

"""output
¡Guau!
Zzz...
"""
