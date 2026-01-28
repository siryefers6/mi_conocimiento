# parametro_ruta__path.py
from fastapi import FastAPI

"""
Objetivo: Capturar parámetros en la ruta URL
Referencia: Parámetros de ruta
Tipo: Parámetro
Nivel: basico
"""

app = FastAPI()

@app.get("/usuarios/{usuario_id}")
def get_usuario(usuario_id: int):
    return {"usuario_id": usuario_id}

@app.get("/posts/{post_id}/comentarios/{comentario_id}")
def get_comentario(post_id: int, comentario_id: int):
    return {"post_id": post_id, "comentario_id": comentario_id}

print("GET /usuarios/123 -> usuario_id = 123")
print("GET /posts/1/comentarios/5 -> post_id = 1, comentario_id = 5")
"""output
{
  "usuario_id": 123
}
"""
