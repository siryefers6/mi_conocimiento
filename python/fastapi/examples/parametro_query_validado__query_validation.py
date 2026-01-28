from fastapi import FastAPI, Query

"""
Objetivo: Validar parámetros query con Query()
Referencia: Query(), parámetros opcionales
Tipo: Validación
Nivel: basico
"""

app = FastAPI()

@app.get("/search")
def buscar(
    q: str = Query(..., min_length=3, max_length=50),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    return {
        "query": q,
        "skip": skip,
        "limit": limit,
        "resultado": f"Buscando '{q}'"
    }

print("GET /search?q=python -> valida min_length=3")
print("GET /search?q=py -> error (menor a 3 caracteres)")
"""output
{
  "query": "python",
  "skip": 0,
  "limit": 10,
  "resultado": "Buscando 'python'"
}
"""
