"""
Objetivo: Ejemplo TDD con lista personalizada
Referencia: Red-Green-Refactor
Tipo: patrón
Nivel: basico
"""

# RED  GREEN  REFACTOR

class MiLista:
    """Implementar lista simple con TDD"""
    
    def __init__(self):
        self.items = []
    
    def agregar(self, item):
        """Agregar elemento"""
        self.items.append(item)
    
    def obtener(self, indice):
        """Obtener elemento por índice"""
        return self.items[indice]
    
    def cantidad(self):
        """Cantidad de elementos"""
        return len(self.items)

# TESTS (Green - todos pasan)
def test_lista_vacia():
    lista = MiLista()
    assert lista.cantidad() == 0

def test_agregar_elemento():
    lista = MiLista()
    lista.agregar("a")
    assert lista.cantidad() == 1

def test_obtener_elemento():
    lista = MiLista()
    lista.agregar("x")
    assert lista.obtener(0) == "x"

def test_agregar_multiples():
    lista = MiLista()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    assert lista.cantidad() == 3
    assert lista.obtener(1) == 2

"""output
test_lista_vacia PASSED
test_agregar_elemento PASSED
test_obtener_elemento PASSED
test_agregar_multiples PASSED
"""
