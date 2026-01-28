"""
Objetivo: Assert para verificar igualdad
Referencia: assert a == b
Tipo: operador
Nivel: basico
"""

def obtener_nombre():
    return "Ana"

def test_nombre_correcto():
    assert obtener_nombre() == "Ana"

def test_nombre_incorrecto():
    nombre = "Juan"
    assert nombre != "Ana"

def test_lista_igual():
    resultado = [1, 2, 3]
    assert resultado == [1, 2, 3]

"""output
test_nombre_correcto PASSED
test_nombre_incorrecto PASSED
test_lista_igual PASSED
"""
