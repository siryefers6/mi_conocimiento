from fastapi import FastAPI
from fastapi.testclient import TestClient

"""
Objetivo: Probar métodos GET con TestClient
Referencia: TestClient, GET requests
Tipo: Testing
Nivel: basico
"""

app = FastAPI()

items = [
    {"id": 1, "nombre": "Laptop"},
    {"id": 2, "nombre": "Mouse"}
]

@app.get("/items")
def listar_items():
    return items

@app.get("/items/{item_id}")
def obtener_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "No encontrado"}

# Testing
client = TestClient(app)

response = client.get("/items")
assert response.status_code == 200
assert len(response.json()) == 2
print("✓ GET /items pasó")

response = client.get("/items/1")
assert response.status_code == 200
assert response.json()["nombre"] == "Laptop"
print("✓ GET /items/1 pasó")

print("Tests exitosos")
"""output
✓ GET /items pasó
✓ GET /items/1 pasó
Tests exitosos
"""
