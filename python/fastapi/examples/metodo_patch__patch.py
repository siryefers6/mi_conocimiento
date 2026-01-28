from fastapi import FastAPI

"""
Objetivo: Actualizar parcialmente un recurso con PATCH
Referencia: @app.patch()
Tipo: Decorador
Nivel: basico
"""

app = FastAPI()
usuario = {"id": 1, "nombre": "Juan", "email": "juan@email.com", "edad": 30}

@app.patch("/usuarios/{usuario_id}")
def partial_update(usuario_id: int, datos: dict):
    usuario.update(datos)
    return {"mensaje": "Usuario actualizado", "usuario": usuario}

print("PATCH /usuarios/1 con {email: nuevo@email.com}")
print("Solo actualiza los campos enviados")
"""output
{
  "mensaje": "Usuario actualizado",
  "usuario": {
    "id": 1,
    "nombre": "Juan",
    "email": "nuevo@email.com",
    "edad": 30
  }
}
"""
