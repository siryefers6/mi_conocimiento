"""
Objetivo: Marcar test como esperado fallar
Referencia: @pytest.mark.xfail
Tipo: decorador
Nivel: basico
"""

import pytest

@pytest.mark.xfail(reason="Bug conocido")
def test_bug_conocido():
    """Test que se espera que falle"""
    # Esto falla, pero está marcado como xfail
    assert 1 == 2

@pytest.mark.xfail
def test_todavia_no_funciona():
    """Otro test esperado fallar"""
    resultado = sum([1, 2, "tres"])  # Error type
    assert resultado == 6

def test_normal_pasa():
    """Test normal"""
    assert 1 + 1 == 2

"""output
test_bug_conocido XFAIL
test_todavia_no_funciona XFAIL
test_normal_pasa PASSED
"""
