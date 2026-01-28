from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

"""
Objetivo: Estructura modular con múltiples archivos
Referencia: APIRouter, include_router
Tipo: Estructura
Nivel: intermedio
"""

# routers/usuarios.py
usuarios_router = APIRouter(prefix="/usuarios", tags=["usuarios"])

class Usuario(BaseModel):
    nombre: str
    email: str

@usuarios_router.get("/")
def listar_usuarios():
    return [{"id": 1, "nombre": "Juan"}]

@usuarios_router.post("/")
def crear_usuario(usuario: Usuario):
    return {"id": 2, **usuario.dict()}

# routers/items.py
items_router = APIRouter(prefix="/items", tags=["items"])

class Item(BaseModel):
    nombre: str
    precio: float

@items_router.get("/")
def listar_items():
    return [{"id": 1, "nombre": "Laptop"}]

@items_router.post("/")
def crear_item(item: Item):
    return {"id": 2, **item.dict()}

# main.py
app = FastAPI(title="API Modular")
app.include_router(usuarios_router)
app.include_router(items_router)

print("Estructura modular")
print("Routers separados por funcionalidad")
"""output
GET /usuarios/
POST /usuarios/
GET /items/
POST /items/
"""
