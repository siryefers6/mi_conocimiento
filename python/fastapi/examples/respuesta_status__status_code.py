from fastapi import FastAPI, HTTPException

"""
Objetivo: Retornar códigos HTTP personalizados
Referencia: status_code parameter
Tipo: Decorador
Nivel: basico
"""

app = FastAPI()

@app.post("/items", status_code=201)
def crear_item(nombre: str):
    return {"mensaje": "Item creado", "nombre": nombre}

@app.delete("/items/{item_id}", status_code=204)
def eliminar_item(item_id: int):
    return None

@app.get("/items/{item_id}", status_code=200)
def obtener_item(item_id: int):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="ID debe ser positivo")
    return {"item_id": item_id}

print("POST /items -> 201 Created")
print("DELETE /items/1 -> 204 No Content")
print("GET /items/0 -> 400 Bad Request")
"""output
{
  "mensaje": "Item creado",
  "nombre": "Laptop"
}
"""
