# parametro_query__query.py
from fastapi import FastAPI

"""
Objetivo: Usar parámetros query string opcionales
Referencia: Query parameters
Tipo: Parámetro
Nivel: basico
"""

app = FastAPI()

@app.get("/search")
def search(q: str = "", skip: int = 0, limit: int = 10):
    return {"query": q, "skip": skip, "limit": limit}

@app.get("/usuarios")
def list_usuarios(skip: int = 0, limit: int = 10):
    usuarios = [{"id": i, "nombre": f"Usuario {i}"} for i in range(100)]
    return usuarios[skip:skip+limit]

print("GET /search?q=python -> {'query': 'python', 'skip': 0, 'limit': 10}")
print("GET /usuarios?skip=5&limit=3 -> Lista usuarios 5-8")
"""output
{
  "query": "python",
  "skip": 0,
  "limit": 10
}
"""
