"""
Objetivo: Usar request fixture para acceder parámetros
Referencia: request.param
Tipo: fixture
Nivel: basico
"""

import pytest

@pytest.fixture(params=[1, 2, 3])
def numero(request):
    """Fixture que proporciona números"""
    return request.param

def test_numero_es_positivo(numero):
    """Test con fixture parametrizada"""
    assert numero > 0

@pytest.fixture(params=[
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Juan", "edad": 25},
])
def usuario(request):
    """Fixture con diccionarios"""
    return request.param

def test_usuario_tiene_nombre(usuario):
    """Test accediendo parámetro"""
    assert "nombre" in usuario
    assert len(usuario["nombre"]) > 0

"""output
test_numero_es_positivo[1] PASSED
test_numero_es_positivo[2] PASSED
test_numero_es_positivo[3] PASSED
test_usuario_tiene_nombre[usuario0] PASSED
test_usuario_tiene_nombre[usuario1] PASSED
"""
