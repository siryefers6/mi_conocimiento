from fastapi import FastAPI
from pydantic import BaseModel, validator

"""
Objetivo: Validadores personalizados en Pydantic
Referencia: @validator decorator
Tipo: Validador
Nivel: intermedio
"""

class Usuario(BaseModel):
    nombre: str
    email: str
    edad: int
    
    @validator('nombre')
    def nombre_no_vacio(cls, v):
        if not v.strip():
            raise ValueError('Nombre no puede estar vacío')
        return v.title()
    
    @validator('edad')
    def edad_valida(cls, v):
        if v < 18:
            raise ValueError('Debe ser mayor de 18 años')
        return v

app = FastAPI()

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    return usuario

print("POST con validadores custom")
print('Valida: nombre no vacío, edad >= 18')
"""output
{
  "nombre": "Juan Pérez",
  "email": "juan@email.com",
  "edad": 25
}
"""
