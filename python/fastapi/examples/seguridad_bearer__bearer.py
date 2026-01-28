from fastapi import FastAPI, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials

"""
Objetivo: Autenticación con Bearer Tokens
Referencia: HTTPBearer, credentials
Tipo: Seguridad
Nivel: intermedio
"""

app = FastAPI()
security = HTTPBearer()

VALID_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

@app.get("/perfil")
async def obtener_perfil(credentials: HTTPAuthCredentials = Depends(security)):
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"usuario": "Juan", "token": credentials.credentials}

print("GET /perfil con header Authorization: Bearer <token>")
print("Valida token en autenticación")
"""output
{
  "usuario": "Juan",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
"""
