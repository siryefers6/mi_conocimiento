from fastapi import FastAPI
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from fastapi import Depends, HTTPException

"""
Objetivo: Guard de autenticación en endpoints
Referencia: Custom dependency para validación
Tipo: Seguridad
Nivel: intermedio
"""

app = FastAPI()
security = HTTPBearer()

VALID_TOKENS = ["token123", "token456"]

def verificar_token(credentials: HTTPAuthCredentials = Depends(security)):
    if credentials.credentials not in VALID_TOKENS:
        raise HTTPException(status_code=401, detail="Token inválido")
    return credentials.credentials

@app.get("/datos-privados")
def obtener_datos_privados(token: str = Depends(verificar_token)):
    return {
        "datos": "secretos",
        "autenticado_con": token
    }

@app.get("/otro-endpoint-protegido")
def otro_endpoint(token: str = Depends(verificar_token)):
    return {"acceso": "concedido"}

print("Guards de autenticación")
print("Reutiliza validación en múltiples endpoints")
"""output
{
  "datos": "secretos",
  "autenticado_con": "token123"
}
"""
