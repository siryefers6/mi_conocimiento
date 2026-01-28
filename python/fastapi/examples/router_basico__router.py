from fastapi import FastAPI, APIRouter

"""
Objetivo: Organizar endpoints con routers
Referencia: APIRouter
Tipo: Estructura
Nivel: intermedio
"""

# Crear routers modulares
usuarios_router = APIRouter(prefix="/usuarios", tags=["usuarios"])
items_router = APIRouter(prefix="/items", tags=["items"])

@usuarios_router.get("/")
def listar_usuarios():
    return [{"id": 1, "nombre": "Juan"}]

@usuarios_router.post("/")
def crear_usuario(nombre: str):
    return {"id": 2, "nombre": nombre}

@items_router.get("/")
def listar_items():
    return [{"id": 1, "nombre": "Laptop"}]

# Crear app y registrar routers
app = FastAPI()
app.include_router(usuarios_router)
app.include_router(items_router)

print("Endpoints organizados con routers")
print("GET /usuarios/")
print("GET /items/")
"""output
[
  {"id": 1, "nombre": "Juan"}
]
"""
