# ruta_get__get.py
from fastapi import FastAPI

"""
Objetivo: Manejar peticiones GET básicas
Referencia: @app.get()
Tipo: Decorador
Nivel: basico
"""

app = FastAPI()

items = {"manzana": 5, "banana": 3, "naranja": 7}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: str):
    if item_id in items:
        return {"item": item_id, "cantidad": items[item_id]}
    return {"error": "Item no encontrado"}

print("GET /items -> Lista todos los items")
print("GET /items/manzana -> Obtiene un item específico")
"""output
{
  "manzana": 5,
  "banana": 3,
  "naranja": 7
}
"""
