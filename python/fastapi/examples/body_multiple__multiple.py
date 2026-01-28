from fastapi import FastAPI
from pydantic import BaseModel

"""
Objetivo: Múltiples parámetros en body request
Referencia: Body with multiple models
Tipo: Validación
Nivel: intermedio
"""

class Item(BaseModel):
    nombre: str
    precio: float

class User(BaseModel):
    nombre: str
    email: str

app = FastAPI()

@app.post("/compra")
def crear_compra(usuario: User, item: Item, cantidad: int = 1):
    return {
        "usuario": usuario,
        "item": item,
        "cantidad": cantidad,
        "total": item.precio * cantidad
    }

print("POST con múltiples bodies")
print('{"usuario": {...}, "item": {...}, "cantidad": 2}')
"""output
{
  "usuario": {
    "nombre": "Juan",
    "email": "juan@email.com"
  },
  "item": {
    "nombre": "Laptop",
    "precio": 999.99
  },
  "cantidad": 2,
  "total": 1999.98
}
"""
