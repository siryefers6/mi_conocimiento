# tipo_datos__typing.py
from fastapi import FastAPI
from typing import Optional

"""
Objetivo: Type hints para validación automática
Referencia: Type hints, Pydantic validation
Tipo: Validación
Nivel: basico
"""

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int, precio: float = 10.5, activo: bool = True):
    return {
        "item_id": item_id,
        "tipo_id": type(item_id).__name__,
        "precio": precio,
        "tipo_precio": type(precio).__name__,
        "activo": activo
    }

print("Validación automática de tipos:")
print("- item_id: int -> valida que sea número entero")
print("- precio: float -> valida que sea número decimal")
print("- activo: bool -> valida que sea booleano")
"""output
{
  "item_id": 1,
  "tipo_id": "int",
  "precio": 10.5,
  "tipo_precio": "float",
  "activo": true
}
"""
