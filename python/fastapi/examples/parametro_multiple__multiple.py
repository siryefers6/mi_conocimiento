# parametro_multiple__multiple.py
from fastapi import FastAPI

"""
Objetivo: Combinar parámetros de ruta y query
Referencia: Multiple parameters
Tipo: Parámetro
Nivel: basico
"""

app = FastAPI()

@app.get("/posts/{post_id}")
def get_post(post_id: int, skip: int = 0, limit: int = 10):
    comentarios = [{"id": i, "texto": f"Comentario {i}"} for i in range(20)]
    return {
        "post_id": post_id,
        "comentarios": comentarios[skip:skip+limit]
    }

print("GET /posts/5?skip=2&limit=3 -> post_id=5 con comentarios 2-4")
"""output
{
  "post_id": 5,
  "comentarios": [...]
}
"""
