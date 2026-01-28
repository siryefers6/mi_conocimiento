from fastapi import FastAPI

"""
Objetivo: Describir parámetros y endpoints
Referencia: docstrings, response_description
Tipo: Documentación
Nivel: basico
"""

app = FastAPI()

@app.get("/items/{item_id}", response_description="Item encontrado")
def obtener_item(item_id: int):
    """
    Obtiene un item específico.
    
    **Parámetros:**
    - item_id: El ID del item (número entero)
    
    **Retorna:**
    - Un diccionario con los datos del item
    """
    return {"item_id": item_id, "nombre": "Laptop"}

@app.post("/items", response_description="Item creado exitosamente")
def crear_item(nombre: str, precio: float):
    """
    Crea un nuevo item.
    
    **Parámetros:**
    - nombre: Nombre del item
    - precio: Precio en dólares
    """
    return {"id": 1, "nombre": nombre, "precio": precio}

print("Descripción en docstrings")
print("Aparece automáticamente en /docs")
"""output
Documentación clara y detallada
Generada desde docstrings Python
"""
