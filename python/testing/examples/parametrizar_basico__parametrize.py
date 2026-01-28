"""
Objetivo: Parametrizar tests con múltiples valores
Referencia: @pytest.mark.parametrize
Tipo: decorador
Nivel: basico
"""

import pytest

def es_par(numero):
    return numero % 2 == 0

@pytest.mark.parametrize("numero,esperado", [
    (2, True),
    (3, False),
    (4, True),
    (5, False),
    (100, True),
])
def test_es_par_parametrizado(numero, esperado):
    """Test que se ejecuta 5 veces con diferentes valores"""
    assert es_par(numero) == esperado

"""output
test_es_par_parametrizado[2-True] PASSED
test_es_par_parametrizado[3-False] PASSED
test_es_par_parametrizado[4-True] PASSED
test_es_par_parametrizado[5-False] PASSED
test_es_par_parametrizado[100-True] PASSED
"""
