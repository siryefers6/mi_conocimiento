from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    precio: float

"""
Objetivo: Reemplazar un recurso completo con PUT
Referencia: @app.put()
Tipo: Decorador
Nivel: basico
"""

app = FastAPI()
items = {"1": {"nombre": "Laptop", "precio": 999.99}}

@app.put("/items/{item_id}")
def update_item(item_id: str, item: Item):
    items[item_id] = item.dict()
    return {"mensaje": "Item actualizado", "item": items[item_id]}

print("PUT /items/1 con body completo")
print("Reemplaza todo el recurso")
"""output
{
  "mensaje": "Item actualizado",
  "item": {
    "nombre": "Laptop gamer",
    "precio": 1299.99
  }
}
"""
