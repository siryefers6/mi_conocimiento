from fastapi import FastAPI

"""
Objetivo: Organizar endpoints con tags
Referencia: tags parameter
Tipo: Documentación
Nivel: basico
"""

app = FastAPI()

@app.get("/items", tags=["items"])
def listar_items():
    """Lista todos los items disponibles"""
    return [{"id": 1, "nombre": "Item 1"}]

@app.post("/items", tags=["items"])
def crear_item(nombre: str):
    """Crea un nuevo item"""
    return {"id": 2, "nombre": nombre}

@app.get("/usuarios", tags=["usuarios"])
def listar_usuarios():
    """Lista todos los usuarios"""
    return [{"id": 1, "nombre": "Juan"}]

@app.post("/usuarios", tags=["usuarios"])
def crear_usuario(nombre: str):
    """Crea un nuevo usuario"""
    return {"id": 2, "nombre": nombre}

print("Tags para organizar documentación")
print("Los endpoints se agrupan en Swagger UI")
"""output
Documentación organizada por tags
Mejora navegación en /docs
"""
