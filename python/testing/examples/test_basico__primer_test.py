"""
Objetivo: Escribir el primer test con pytest
Referencia: def test_
Tipo: función
Nivel: basico
"""

def suma(a, b):
    return a + b

def test_suma_positivos():
    """Test de suma con números positivos"""
    resultado = suma(2, 3)
    assert resultado == 5

def test_suma_negativos():
    """Test de suma con números negativos"""
    resultado = suma(-1, -2)
    assert resultado == -3

def test_suma_mixtos():
    """Test de suma con números mixtos"""
    resultado = suma(5, -3)
    assert resultado == 2

# EJECUTAR CON: pytest test_basico__primer_test.py -v

"""output
test_basico__primer_test.py::test_suma_positivos PASSED
test_basico__primer_test.py::test_suma_negativos PASSED
test_basico__primer_test.py::test_suma_mixtos PASSED
"""
