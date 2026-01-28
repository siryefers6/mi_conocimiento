"""
Objetivo: Usar conftest.py para fixtures compartidas
Referencia: conftest.py
Tipo: archivo
Nivel: basico
"""

# conftest.py es archivo especial de pytest
# Se busca automáticamente en directorios
# Contiene fixtures compartidas entre tests

# ESTRUCTURA:
# proyecto/
#   conftest.py (fixtures globales)
#   tests/
#     conftest.py (fixtures para tests/)
#     test_suma.py
#     test_resta.py

# EJEMPLO DE conftest.py:

import pytest

@pytest.fixture
def usuario_base():
    """Fixture global para todos los tests"""
    return {
        "id": 1,
        "nombre": "Ana",
        "email": "ana@example.com"
    }

@pytest.fixture
def base_de_datos():
    """Conectar antes del test"""
    print("Conectando a BD...")
    db = {"conectado": True}
    yield db
    print("Desconectando...")

# Ahora cualquier test puede usar estas fixtures:
# def test_usuario(usuario_base):
#     assert usuario_base["nombre"] == "Ana"

# def test_db(base_de_datos):
#     assert base_de_datos["conectado"]

"""
