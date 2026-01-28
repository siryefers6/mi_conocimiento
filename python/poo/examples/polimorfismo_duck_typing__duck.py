"""
Objetivo: Implementar polimorfismo con duck typing
Referencia: duck typing
Tipo: patrón
Nivel: basico
"""

class Perro:
    def hacer_sonido(self):
        return "¡Guau!"

class Gato:
    def hacer_sonido(self):
        return "¡Miau!"

class Vaca:
    def hacer_sonido(self):
        return "¡Muuu!"

def escuchar_sonido(animal):
    print(animal.hacer_sonido())

# funciona con cualquier objeto que tenga hacer_sonido
escuchar_sonido(Perro())
escuchar_sonido(Gato())
escuchar_sonido(Vaca())

"""output
¡Guau!
¡Miau!
¡Muuu!
"""
