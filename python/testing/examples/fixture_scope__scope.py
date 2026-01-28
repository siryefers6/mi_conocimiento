"""
Objetivo: Fixture con scope para reutilizar
Referencia: scope="module"
Tipo: parámetro
Nivel: basico
"""

import pytest

@pytest.fixture(scope="function")  # default: se crea para cada test
def contador_function():
    contador = {"valor": 0}
    contador["valor"] += 1
    return contador

@pytest.fixture(scope="module")  # se crea una sola vez para el módulo
def conexion_db():
    print("\\nConectando a BD...")
    conexion = {"conectado": True}
    yield conexion
    print("\\nDesconectando de BD...")

def test_contador_1(contador_function):
    """Primer contador"""
    assert contador_function["valor"] == 1

def test_contador_2(contador_function):
    """Segundo contador (nuevo)"""
    assert contador_function["valor"] == 1  # Nueva instancia

def test_db_1(conexion_db):
    """Primer test con BD"""
    assert conexion_db["conectado"]

def test_db_2(conexion_db):
    """Segundo test (misma BD)"""
    assert conexion_db["conectado"]

"""output
test_contador_1 PASSED
test_contador_2 PASSED
test_db_1 PASSED (conexión abierta)
test_db_2 PASSED (misma conexión)
Desconectando de BD...
"""
