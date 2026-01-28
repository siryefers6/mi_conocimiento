"""
Objetivo: Implementar __call__ para objetos invocables
Referencia: __call__
Tipo: método especial
Nivel: basico
"""

class Multiplicador:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

duplo = Multiplicador(2)
print(f"5 * 2 = {duplo(5)}")

triple = Multiplicador(3)
print(f"5 * 3 = {triple(5)}")

# como función
resultado = duplo(10)
print(f"10 * 2 = {resultado}")

"""output
5 * 2 = 10
5 * 3 = 15
10 * 2 = 20
"""
