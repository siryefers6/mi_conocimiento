"""
Objetivo: Fixture que retorna datos
Referencia: return datos
Tipo: keyword
Nivel: basico
"""

import pytest

@pytest.fixture
def calculadora():
    """Fixture que retorna una clase"""
    class Calculadora:
        def sumar(self, a, b):
            return a + b
        def multiplicar(self, a, b):
            return a * b
    return Calculadora()

def test_suma(calculadora):
    """Usar fixture de clase"""
    assert calculadora.sumar(2, 3) == 5

def test_multiplicacion(calculadora):
    """Otra operación"""
    assert calculadora.multiplicar(3, 4) == 12

"""output
test_suma PASSED
test_multiplicacion PASSED
"""
