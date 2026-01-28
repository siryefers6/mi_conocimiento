"""
Objetivo: Fixture parametrizada
Referencia: params=[]
Tipo: parámetro
Nivel: basico
"""

import pytest

@pytest.fixture(params=["Ana", "Juan", "Carlos"])
def nombre(request):
    """Fixture que proporciona múltiples valores"""
    return request.param

def test_nombre_no_vacio(nombre):
    """Test se ejecuta 3 veces, una por cada nombre"""
    assert len(nombre) > 0
    print(f"Testing con: {nombre}")

@pytest.fixture(params=[
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Juan"},
])
def usuario(request):
    """Fixture con objetos complejos"""
    return request.param

def test_usuario_id(usuario):
    """Tests con usuarios diferentes"""
    assert "id" in usuario
    assert usuario["id"] > 0

"""output
test_nombre_no_vacio[Ana] PASSED
test_nombre_no_vacio[Juan] PASSED
test_nombre_no_vacio[Carlos] PASSED
test_usuario_id[usuario0] PASSED
test_usuario_id[usuario1] PASSED
"""
