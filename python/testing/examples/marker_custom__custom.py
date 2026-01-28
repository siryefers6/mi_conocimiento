"""
Objetivo: Crear markers personalizados
Referencia: @pytest.mark.custom
Tipo: decorador
Nivel: basico
"""

import pytest

@pytest.mark.slow
def test_operacion_lenta():
    """Test lento - se puede saltar"""
    import time
    time.sleep(1)
    assert True

@pytest.mark.fast
def test_operacion_rapida():
    """Test rápido"""
    assert 1 + 1 == 2

@pytest.mark.integration
def test_integracion():
    """Test de integración"""
    # Requiere BD, API, etc
    assert True

# EJECUTAR SOLO TESTS RÁPIDOS:
# pytest test_basico__primer_test.py -m fast

# EJECUTAR EXCEPTO LENTOS:
# pytest test_basico__primer_test.py -m "not slow"

"""output
test_operacion_lenta PASSED
test_operacion_rapida PASSED
test_integracion PASSED
"""
