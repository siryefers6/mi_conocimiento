"""
Objetivo: Test para verificar ValueError específico
Referencia: ValueError
Tipo: excepción
Nivel: basico
"""

import pytest

def validar_numero_positivo(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Debe ser número")
    if n <= 0:
        raise ValueError("Debe ser positivo")
    return n

def test_error_tipo():
    """Verificar TypeError"""
    with pytest.raises(TypeError):
        validar_numero_positivo("texto")

def test_error_valor():
    """Verificar ValueError"""
    with pytest.raises(ValueError):
        validar_numero_positivo(-5)

def test_numero_valido():
    """Test que funciona"""
    assert validar_numero_positivo(10) == 10

"""output
test_error_tipo PASSED
test_error_valor PASSED
test_numero_valido PASSED
"""
