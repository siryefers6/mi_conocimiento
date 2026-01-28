"""
Objetivo: Saltar tests con @pytest.mark.skip
Referencia: @pytest.mark.skip
Tipo: decorador
Nivel: basico
"""

import pytest

@pytest.mark.skip(reason="Feature no implementado aún")
def test_feature_nueva():
    """Este test se salta"""
    pass

@pytest.mark.skip
def test_pendiente():
    """Test sin implementar"""
    assert False

def test_normal():
    """Test que sí se ejecuta"""
    assert True

"""output
test_feature_nueva SKIPPED
test_pendiente SKIPPED
test_normal PASSED
"""
