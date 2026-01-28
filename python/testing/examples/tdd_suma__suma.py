"""
Objetivo: Ejemplo de TDD simple - Suma
Referencia: Red-Green-Refactor
Tipo: patrón
Nivel: basico
"""

# RED: Test que falla (comentado porque falla)
# def test_suma_basica():
#     from suma import sumar
#     assert sumar(2, 3) == 5

# GREEN: Código mínimo para pasar test
def sumar(a, b):
    return a + b

# Tests que PASAN
def test_suma_basica():
    assert sumar(2, 3) == 5

def test_suma_negativos():
    assert sumar(-1, -1) == -2

def test_suma_cero():
    assert sumar(0, 5) == 5

# REFACTOR: Mejorar el código
# (En este caso, el código ya está bien)

"""output
test_suma_basica PASSED
test_suma_negativos PASSED
test_suma_cero PASSED
"""
