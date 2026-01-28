from fastapi import FastAPI, Query, Depends

"""
Objetivo: Dependencias en parámetros query
Referencia: Query() como dependencia
Tipo: Patrón
Nivel: intermedio
"""

class PaginacionParams:
    def __init__(self, skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
        self.skip = skip
        self.limit = limit

app = FastAPI()

@app.get("/items")
def listar_items(params: PaginacionParams = Depends()):
    items = [f"Item {i}" for i in range(params.skip, params.skip + params.limit)]
    return {
        "items": items,
        "skip": params.skip,
        "limit": params.limit
    }

print("Dependencias en query")
print("GET /items?skip=0&limit=5")
"""output
{
  "items": ["Item 0", "Item 1", "Item 2", "Item 3", "Item 4"],
  "skip": 0,
  "limit": 5
}
"""
