"""
Objetivo: Fixture autouse que se ejecuta automáticamente
Referencia: autouse=True
Tipo: parámetro
Nivel: basico
"""

import pytest

@pytest.fixture(autouse=True)
def setup_teardown():
    """Se ejecuta antes de cada test automáticamente"""
    print("\\nSetup: preparar test")
    yield
    print("\\nTeardown: limpiar después test")

def test_uno():
    """Test que usa fixture sin pedir"""
    assert True

def test_dos():
    """Otro test"""
    assert 1 + 1 == 2

"""output
Setup: preparar test
test_uno PASSED
Teardown: limpiar después test
Setup: preparar test
test_dos PASSED
Teardown: limpiar después test
"""
