"""
Objetivo: Usar assert para verificaciones básicas
Referencia: assert
Tipo: keyword
Nivel: basico
"""

def es_par(numero):
    return numero % 2 == 0

def test_numero_par():
    """Verificar que 4 es par"""
    assert es_par(4)

def test_numero_impar():
    """Verificar que 5 no es par"""
    assert not es_par(5)

def test_numero_grande_es_par():
    """Verificar número grande"""
    assert es_par(1000)

"""output
test_numero_par PASSED
test_numero_impar PASSED
test_numero_grande_es_par PASSED
"""
