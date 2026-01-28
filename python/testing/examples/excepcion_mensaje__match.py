"""
Objetivo: Test verificando mensaje de excepción
Referencia: match=
Tipo: parámetro
Nivel: basico
"""

import pytest

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 150:
        raise ValueError("La edad no es realista")
    return edad

def test_excepcion_negativa():
    """Verificar mensaje específico"""
    with pytest.raises(ValueError, match="no puede ser negativa"):
        validar_edad(-5)

def test_excepcion_realista():
    """Otro mensaje"""
    with pytest.raises(ValueError, match="no es realista"):
        validar_edad(200)

"""output
test_excepcion_negativa PASSED
test_excepcion_realista PASSED
"""
