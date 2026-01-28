from fastapi import FastAPI
from typing import Optional

"""
Objetivo: Parámetros opcionales en modelo
Referencia: Optional, default values
Tipo: Modelo
Nivel: basico
"""

class Item(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    impuesto: Optional[float] = None

from pydantic import BaseModel

app = FastAPI()

@app.post("/items")
def crear_item(item: Item):
    return item

print("POST con parámetros opcionales")
print('descripcion e impuesto son opcionales')
"""output
{
  "nombre": "Laptop",
  "descripcion": null,
  "precio": 999.99,
  "impuesto": null
}
"""
