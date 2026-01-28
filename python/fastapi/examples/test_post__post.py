from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

"""
Objetivo: Probar métodos POST con TestClient
Referencia: TestClient, POST requests
Tipo: Testing
Nivel: basico
"""

class Item(BaseModel):
    nombre: str
    precio: float

app = FastAPI()
items = []

@app.post("/items")
def crear_item(item: Item):
    items.append(item.dict())
    return item

# Testing
client = TestClient(app)

response = client.post(
    "/items",
    json={"nombre": "Laptop", "precio": 999.99}
)

assert response.status_code == 200
assert response.json()["nombre"] == "Laptop"
print("✓ POST /items pasó")

assert len(items) == 1
print("✓ Item fue agregado")

print("Tests POST exitosos")
"""output
✓ POST /items pasó
✓ Item fue agregado
Tests POST exitosos
"""
