from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

"""
Objetivo: Usar fixtures en tests de FastAPI
Referencia: pytest fixtures, conftest
Tipo: Testing
Nivel: intermedio
"""

app = FastAPI()

usuarios = {
    1: {"id": 1, "nombre": "Juan"}
}

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    return usuarios.get(usuario_id)

@pytest.fixture
def client():
    return TestClient(app)

def test_obtener_usuario(client):
    response = client.get("/usuarios/1")
    assert response.status_code == 200
    assert response.json()["nombre"] == "Juan"

def test_usuario_no_existe(client):
    response = client.get("/usuarios/999")
    assert response.status_code == 200
    assert response.json() is None

print("Tests con fixtures")
print("Fixture client disponible para múltiples tests")
"""output
Tests con fixtures ejecutándose
Fixture simplifica setup y teardown
"""
