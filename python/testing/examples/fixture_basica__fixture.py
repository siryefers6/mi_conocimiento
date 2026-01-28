"""
Objetivo: Usar fixture básica para preparar datos
Referencia: @pytest.fixture
Tipo: decorador
Nivel: basico
"""

import pytest

@pytest.fixture
def usuario():
    """Fixture que proporciona un usuario"""
    return {"id": 1, "nombre": "Ana", "email": "ana@email.com"}

def test_usuario_tiene_nombre(usuario):
    """Test que usa la fixture"""
    assert usuario["nombre"] == "Ana"

def test_usuario_tiene_email(usuario):
    """Otro test usando la misma fixture"""
    assert usuario["email"] == "ana@email.com"

"""output
test_usuario_tiene_nombre PASSED
test_usuario_tiene_email PASSED
"""
