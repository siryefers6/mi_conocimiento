"""
Objetivo: Fixture factory para generar múltiples datos
Referencia: factory function
Tipo: patrón
Nivel: basico
"""

import pytest

@pytest.fixture
def usuario_factory():
    """Factory que genera usuarios"""
    def _crear_usuario(nombre="Ana", edad=30, admin=False):
        return {
            "nombre": nombre,
            "edad": edad,
            "admin": admin
        }
    return _crear_usuario

def test_usuario_normal(usuario_factory):
    """Usar factory para crear usuario normal"""
    usuario = usuario_factory()
    assert usuario["nombre"] == "Ana"
    assert usuario["admin"] == False

def test_usuario_admin(usuario_factory):
    """Usar factory para crear admin"""
    admin = usuario_factory(nombre="Bob", admin=True)
    assert admin["admin"] == True

def test_multiples_usuarios(usuario_factory):
    """Factory para crear múltiples usuarios"""
    usuarios = [
        usuario_factory(nombre="Ana"),
        usuario_factory(nombre="Juan"),
        usuario_factory(nombre="Carlos"),
    ]
    assert len(usuarios) == 3

"""output
test_usuario_normal PASSED
test_usuario_admin PASSED
test_multiples_usuarios PASSED
"""
