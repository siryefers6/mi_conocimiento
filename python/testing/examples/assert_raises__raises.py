"""
Objetivo: Assert para verificar excepciones
Referencia: pytest.raises()
Tipo: función
Nivel: basico
"""

import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def test_excepcion_division_cero():
    """Verificar que se lanza ValueError"""
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_excepcion_tipo_correcto():
    """Verificar tipo de excepción"""
    with pytest.raises(ZeroDivisionError):
        resultado = 1 / 0

"""output
test_excepcion_division_cero PASSED
test_excepcion_tipo_correcto PASSED
"""
