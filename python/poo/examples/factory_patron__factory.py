"""
Objetivo: Implementar patrón Factory
Referencia: Factory
Tipo: patrón
Nivel: basico
"""

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

class AnimalFactory:
    @staticmethod
    def crear_animal(tipo: str) -> Animal:
        if tipo == "perro":
            return Perro()
        elif tipo == "gato":
            return Gato()
        else:
            raise ValueError(f"Tipo desconocido: {tipo}")

# usar factory
perro = AnimalFactory.crear_animal("perro")
print(perro.hacer_sonido())

gato = AnimalFactory.crear_animal("gato")
print(gato.hacer_sonido())

"""output
¡Guau!
¡Miau!
"""
