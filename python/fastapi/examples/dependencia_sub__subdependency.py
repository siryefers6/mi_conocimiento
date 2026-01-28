from fastapi import FastAPI, Depends

"""
Objetivo: Sub-dependencias (dependencias anidadas)
Referencia: Nested dependencies
Tipo: Patrón
Nivel: intermedio
"""

def obtener_query_param(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

def obtener_parametros_paginacion(
    params: dict = Depends(obtener_query_param)
):
    return {
        "skip": params["skip"],
        "limit": params["limit"],
        "valido": params["skip"] >= 0 and params["limit"] > 0
    }

app = FastAPI()

@app.get("/items")
def listar_items(
    paginacion = Depends(obtener_parametros_paginacion)
):
    return {
        "items": [1, 2, 3],
        "paginacion": paginacion
    }

print("Sub-dependencias")
print("GET /items?skip=0&limit=10")
"""output
{
  "items": [1, 2, 3],
  "paginacion": {
    "skip": 0,
    "limit": 10,
    "valido": true
  }
}
"""
