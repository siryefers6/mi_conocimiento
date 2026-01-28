"""
Objetivo: Assert para números flotantes con tolerancia
Referencia: pytest.approx()
Tipo: función
Nivel: basico
"""

import pytest

def calcular_pi():
    return 3.14159265

def test_float_exacto():
    """Comparar floats con tolerancia"""
    resultado = calcular_pi()
    assert resultado == pytest.approx(3.14159, rel=1e-5)

def test_listas_floats():
    """Comparar listas de floats"""
    resultados = [1.001, 2.002, 3.003]
    esperados = [1.0, 2.0, 3.0]
    
    # Sin approx fallaría
    assert resultados == pytest.approx(esperados, abs=0.01)

"""output
test_float_exacto PASSED
test_listas_floats PASSED
"""
