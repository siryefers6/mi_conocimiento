"""
Objetivo: Parametrizar con IDs personalizados
Referencia: ids=[]
Tipo: parámetro
Nivel: basico
"""

import pytest

@pytest.mark.parametrize("edad,es_adulto", [
    (15, False),
    (18, True),
    (65, True),
    (5, False),
], ids=["adolescente", "joven_adulto", "adulto_mayor", "niño"])
def test_es_adulto(edad, es_adulto):
    """Test con IDs descriptivos"""
    resultado = edad >= 18
    assert resultado == es_adulto

"""output
test_es_adulto[adolescente] PASSED
test_es_adulto[joven_adulto] PASSED
test_es_adulto[adulto_mayor] PASSED
test_es_adulto[niño] PASSED
"""
