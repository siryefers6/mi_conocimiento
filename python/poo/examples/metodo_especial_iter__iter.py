"""
Objetivo: Implementar __iter__ para iteración
Referencia: __iter__
Tipo: método especial
Nivel: basico
"""

class Rango:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin
        self.actual = inicio
    
    def __iter__(self):
        self.actual = self.inicio
        return self
    
    def __next__(self):
        if self.actual >= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor

r = Rango(1, 4)
for valor in r:
    print(f"Valor: {valor}")

"""output
Valor: 1
Valor: 2
Valor: 3
"""
