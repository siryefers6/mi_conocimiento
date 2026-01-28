from fastapi import FastAPI

"""
Objetivo: Eliminar un recurso con DELETE
Referencia: @app.delete()
Tipo: Decorador
Nivel: basico
"""

app = FastAPI()
items = {"1": "Laptop", "2": "Mouse", "3": "Teclado"}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id in items:
        nombre = items.pop(item_id)
        return {"mensaje": f"Item {nombre} eliminado"}
    return {"error": "Item no encontrado"}

print("DELETE /items/1 -> elimina el item")
print("DELETE /items/999 -> error no encontrado")
"""output
{
  "mensaje": "Item Laptop eliminado"
}
"""
