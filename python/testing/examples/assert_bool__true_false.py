"""
Objetivo: Assert para verificar booleanos
Referencia: assert bool
Tipo: operador
Nivel: basico
"""

def es_mayor_edad(edad):
    return edad >= 18

def test_es_mayor_edad():
    """Test que es True"""
    assert es_mayor_edad(25) is True

def test_no_es_mayor_edad():
    """Test que es False"""
    assert es_mayor_edad(15) is False

def test_valor_verdadero():
    """Test con valor truthy"""
    assert "texto"  # No vacío es truthy
    assert [1, 2, 3]  # Lista no vacía es truthy

def test_valor_falso():
    """Test con valor falsy"""
    assert not ""  # String vacío es falsy
    assert not []  # Lista vacía es falsy
    assert not 0  # Cero es falsy

"""output
test_es_mayor_edad PASSED
test_no_es_mayor_edad PASSED
test_valor_verdadero PASSED
test_valor_falso PASSED
"""
