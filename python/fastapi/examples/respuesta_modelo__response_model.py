from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    email: str

"""
Objetivo: Especificar modelo de respuesta
Referencia: response_model parameter
Tipo: Decorador
Nivel: basico
"""

app = FastAPI()

usuarios = {
    1: {"id": 1, "nombre": "Juan", "email": "juan@email.com", "password": "secret"}
}

@app.get("/usuarios/{usuario_id}", response_model=Usuario)
def obtener_usuario(usuario_id: int):
    usuario = usuarios.get(usuario_id)
    if not usuario:
        return {"error": "No encontrado"}
    return usuario

print("Respuesta model oculta campos sensibles como password")
print("GET /usuarios/1")
"""output
{
  "id": 1,
  "nombre": "Juan",
  "email": "juan@email.com"
}
"""
