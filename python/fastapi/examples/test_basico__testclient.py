from fastapi import FastAPI
from fastapi.testclient import TestClient

"""
Objetivo: Probar endpoints con TestClient
Referencia: TestClient
Tipo: Testing
Nivel: basico
"""

app = FastAPI()

@app.get("/items/{item_id}")
def obtener_item(item_id: int):
    return {"item_id": item_id, "nombre": "Laptop"}

# Testing
client = TestClient(app)
response = client.get("/items/1")

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

assert response.status_code == 200
assert response.json()["item_id"] == 1
print("✓ Tests pasaron")
"""output
Status: 200
Response: {'item_id': 1, 'nombre': 'Laptop'}
✓ Tests pasaron
"""
