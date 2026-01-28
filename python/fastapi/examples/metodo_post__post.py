from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    precio: float
    descripcion: str = None

"""
Objetivo: Manejar peticiones POST para crear recursos
Referencia: @app.post()
Tipo: Decorador
Nivel: basico
"""

app = FastAPI()
items = []

@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return {"mensaje": "Item creado", "item": item}

print("POST /items con body:")
print('{"nombre": "Laptop", "precio": 999.99}')
"""output
{
  "mensaje": "Item creado",
  "item": {
    "nombre": "Laptop",
    "precio": 999.99,
    "descripcion": null
  }
}
"""
