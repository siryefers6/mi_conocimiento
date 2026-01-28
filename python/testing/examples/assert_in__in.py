"""
Objetivo: Assert para verificar pertenencia
Referencia: assert x in lista
Tipo: operador
Nivel: basico
"""

def test_numero_en_lista():
    """Verificar que un número está en lista"""
    numeros = [1, 2, 3, 4, 5]
    assert 3 in numeros

def test_string_en_lista():
    """Verificar string en lista"""
    palabras = ["gato", "perro", "pájaro"]
    assert "gato" in palabras

def test_numero_no_en_lista():
    """Verificar número NO está en lista"""
    assert 10 not in [1, 2, 3, 4, 5]

"""output
test_numero_en_lista PASSED
test_string_en_lista PASSED
test_numero_no_en_lista PASSED
"""
