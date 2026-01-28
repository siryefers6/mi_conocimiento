"""
Objetivo: Parametrizar con dos parámetros
Referencia: @pytest.mark.parametrize (múltiple)
Tipo: decorador
Nivel: basico
"""

import pytest

@pytest.mark.parametrize("a,b,suma_esperada", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_suma(a, b, suma_esperada):
    """Test con múltiples parámetros"""
    assert a + b == suma_esperada

# También puedes anidar parametrización
@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [10, 20])
def test_multiplicacion_anidada(x, y):
    """Se ejecuta 3 * 2 = 6 veces"""
    resultado = x * y
    assert resultado > 0

"""output
test_suma[1-2-3] PASSED
test_suma[5-5-10] PASSED
test_suma[-1-1-0] PASSED
test_suma[100-200-300] PASSED
test_multiplicacion_anidada[1-10] PASSED
test_multiplicacion_anidada[1-20] PASSED
test_multiplicacion_anidada[2-10] PASSED
test_multiplicacion_anidada[2-20] PASSED
test_multiplicacion_anidada[3-10] PASSED
test_multiplicacion_anidada[3-20] PASSED
"""
