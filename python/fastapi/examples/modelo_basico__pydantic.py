from fastapi import FastAPI
from pydantic import BaseModel, Field

"""
Objetivo: Validar campos con Pydantic
Referencia: BaseModel, Field, validators
Tipo: Modelo
Nivel: basico
"""

class Producto(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    precio: float = Field(..., gt=0)
    stock: int = Field(default=0, ge=0)

app = FastAPI()

@app.post("/productos")
def crear_producto(producto: Producto):
    return {
        "mensaje": "Producto creado",
        "datos": producto,
        "valido": True
    }

print("POST con validación:")
print('{"nombre": "Laptop", "precio": 999.99, "stock": 5}')
"""output
{
  "mensaje": "Producto creado",
  "datos": {
    "nombre": "Laptop",
    "precio": 999.99,
    "stock": 5
  },
  "valido": true
}
"""
