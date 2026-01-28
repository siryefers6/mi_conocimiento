from fastapi import FastAPI
from pydantic import BaseModel

"""
Objetivo: Validación de body request
Referencia: Body, ejemplos en schema
Tipo: Validación
Nivel: basico
"""

class Item(BaseModel):
    nombre: str
    descripcion: str = None
    precio: float
    impuesto: float = None
    
    class Config:
        schema_extra = {
            "example": {
                "nombre": "Laptop",
                "descripcion": "Laptop de 15 pulgadas",
                "precio": 999.99,
                "impuesto": 99.99
            }
        }

app = FastAPI()

@app.post("/items")
def crear_item(item: Item):
    return item

print("Validación de request body")
print("Con ejemplos en OpenAPI")
"""output
{
  "nombre": "Laptop",
  "descripcion": "Laptop de 15 pulgadas",
  "precio": 999.99,
  "impuesto": 99.99
}
"""
