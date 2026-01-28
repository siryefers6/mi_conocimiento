from fastapi import FastAPI, Depends

"""
Objetivo: Usar inyección de dependencias
Referencia: Depends(), función como dependencia
Tipo: Patrón
Nivel: basico
"""

def obtener_token_usuario(token: str = None):
    if not token:
        return None
    return {"usuario_id": 1, "token": token}

app = FastAPI()

@app.get("/items")
def listar_items(usuario = Depends(obtener_token_usuario)):
    if not usuario:
        return {"error": "No autenticado"}
    return {"usuario": usuario, "items": []}

print("GET /items?token=abc123")
print("Las dependencias se ejecutan automáticamente")
"""output
{
  "usuario": {
    "usuario_id": 1,
    "token": "abc123"
  },
  "items": []
}
"""
