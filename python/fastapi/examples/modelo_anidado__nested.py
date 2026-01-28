from fastapi import FastAPI
from pydantic import BaseModel

"""
Objetivo: Modelos anidados con Pydantic
Referencia: Nested models
Tipo: Modelo
Nivel: intermedio
"""

class Direccion(BaseModel):
    calle: str
    ciudad: str
    pais: str

class Usuario(BaseModel):
    nombre: str
    email: str
    direccion: Direccion

app = FastAPI()

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return {
        "usuario": usuario.nombre,
        "ubicacion": f"{usuario.direccion.ciudad}, {usuario.direccion.pais}"
    }

print("POST con modelo anidado")
print('direccion es un objeto dentro de usuario')
"""output
{
  "usuario": "Juan",
  "ubicacion": "Madrid, España"
}
"""
