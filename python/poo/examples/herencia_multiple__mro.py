"""
Objetivo: Implementar herencia múltiple
Referencia: class Hija(Padre1, Padre2)
Tipo: keyword
Nivel: basico
"""

class Volador:
    def volar(self):
        return "Volando..."

class Nadador:
    def nadar(self):
        return "Nadando..."

class Pato(Volador, Nadador):
    def quack(self):
        return "¡Cuac!"

pato = Pato()
print(pato.volar())
print(pato.nadar())
print(pato.quack())

# orden de resolución
print(f"MRO: {[c.__name__ for c in Pato.__mro__]}")

"""output
Volando...
Nadando...
¡Cuac!
MRO: ['Pato', 'Volador', 'Nadador', 'object']
"""
