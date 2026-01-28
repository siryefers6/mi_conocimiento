from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

"""
Objetivo: Tests parametrizados en FastAPI
Referencia: @pytest.mark.parametrize
Tipo: Testing
Nivel: intermedio
"""

app = FastAPI()

@app.get("/items/{item_id}")
def obtener_item(item_id: int):
    items = {
        1: "Laptop",
        2: "Mouse",
        3: "Teclado"
    }
    return {"item_id": item_id, "nombre": items.get(item_id)}

client = TestClient(app)

@pytest.mark.parametrize("item_id,nombre", [
    (1, "Laptop"),
    (2, "Mouse"),
    (3, "Teclado"),
])
def test_obtener_items(item_id, nombre):
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["nombre"] == nombre

print("Tests parametrizados")
print("Ejecuta el mismo test con diferentes valores")
"""output
Test ejecutado 3 veces con diferentes items
Útil para probar múltiples casos
"""
