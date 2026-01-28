from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import Optional

"""
Objetivo: Validar campos complejos
Referencia: @validator con múltiples campos
Tipo: Validación
Nivel: intermedio
"""

class Producto(BaseModel):
    nombre: str
    precio: float
    descuento: Optional[float] = None
    
    @validator('nombre')
    def nombre_minimo(cls, v):
        if len(v) < 3:
            raise ValueError('Nombre debe tener al menos 3 caracteres')
        return v
    
    @validator('descuento')
    def descuento_valido(cls, v, values):
        if v and v > values.get('precio', 0):
            raise ValueError('Descuento no puede ser mayor al precio')
        return v

app = FastAPI()

@app.post("/productos")
def crear_producto(producto: Producto):
    return producto

print("Validación compleja con validators")
print("Valida relaciones entre campos")
"""output
{
  "nombre": "Laptop",
  "precio": 999.99,
  "descuento": 100.0
}
"""
