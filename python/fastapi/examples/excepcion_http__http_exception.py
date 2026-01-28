from fastapi import FastAPI, HTTPException

"""
Objetivo: Lanzar excepciones HTTP
Referencia: HTTPException
Tipo: Excepción
Nivel: basico
"""

app = FastAPI()

usuarios = {1: "Juan", 2: "Maria"}

@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    if usuario_id not in usuarios:
        raise HTTPException(
            status_code=404,
            detail=f"Usuario {usuario_id} no encontrado"
        )
    return {"usuario": usuarios[usuario_id]}

print("GET /usuarios/999 -> lanza 404")
print("GET /usuarios/1 -> retorna usuario")
"""output
{
  "detail": "Usuario 999 no encontrado"
}
"""
