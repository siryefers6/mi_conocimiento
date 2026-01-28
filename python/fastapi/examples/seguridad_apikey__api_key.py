from fastapi import FastAPI
from fastapi.security import APIKeyHeader, APIKeyQuery

"""
Objetivo: Autenticación con API Key
Referencia: APIKeyHeader, APIKeyQuery
Tipo: Seguridad
Nivel: intermedio
"""

app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key")

VALID_API_KEY = "sk-1234567890"

@app.get("/datos")
def obtener_datos(api_key: str = Depends(api_key_header)):
    if api_key != VALID_API_KEY:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return {"datos": "secretos"}

from fastapi import Depends, HTTPException

print("GET /datos con header X-API-Key")
print("Si la key es inválida: 403 Forbidden")
"""output
{
  "datos": "secretos"
}
"""
