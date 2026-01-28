"""
Objetivo: Fallar test manualmente
Referencia: pytest.fail()
Tipo: función
Nivel: basico
"""

import pytest

def test_fallo_manual():
    """Fallar test conscientemente"""
    if True:
        pytest.fail("Este test falla a propósito")

def test_con_condicional():
    """Fallar si ocurre algo inesperado"""
    resultado = 1 + 1
    if resultado != 2:
        pytest.fail(f"Resultado inesperado: {resultado}")
    else:
        pass  # Test pasa

"""output
test_fallo_manual FAILED (por diseño)
test_con_condicional PASSED
"""
