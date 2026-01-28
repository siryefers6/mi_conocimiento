from fastapi import FastAPI

"""
Objetivo: Body básico - recibir JSON
Referencia: Request body, Pydantic models
Tipo: Body request
Nivel: basico
"""

from pydantic import BaseModel

class Item(BaseModel):
    nombre: str
    descripcion: str = None
    precio: float

app = FastAPI()

@app.post("/items")
def crear_item(item: Item):
    return {
        "mensaje": "Item creado",
        "item": item
    }

print("Body básico")
print('POST {"nombre": "Laptop", "precio": 999.99}')
"""output
{
  "mensaje": "Item creado",
  "item": {
    "nombre": "Laptop",
    "descripcion": null,
    "precio": 999.99
  }
}
"""
