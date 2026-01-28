from fastapi import FastAPI
from fastapi.responses import FileResponse

"""
Objetivo: Retornar diferentes tipos de respuesta
Referencia: response_model, FileResponse, JSONResponse
Tipo: Respuesta
Nivel: intermedio
"""

app = FastAPI()

@app.get("/items", response_model=list)
def listar_items():
    return [
        {"id": 1, "nombre": "Item 1"},
        {"id": 2, "nombre": "Item 2"}
    ]

@app.get("/items/{item_id}")
def obtener_item(item_id: int):
    return {"id": item_id, "nombre": f"Item {item_id}"}

print("GET /items -> retorna lista")
print("GET /items/1 -> retorna un item")
"""output
[
  {"id": 1, "nombre": "Item 1"},
  {"id": 2, "nombre": "Item 2"}
]
"""
