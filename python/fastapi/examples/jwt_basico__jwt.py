from fastapi import FastAPI
from datetime import datetime, timedelta
import jwt

"""
Objetivo: Usar JWT para autenticación
Referencia: PyJWT, encode/decode
Tipo: Seguridad
Nivel: avanzado
"""

app = FastAPI()
SECRET_KEY = "tu-clave-secreta-aqui"

def crear_jwt(usuario_id: int):
    payload = {
        "usuario_id": usuario_id,
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verificar_jwt(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.InvalidTokenError:
        return None

@app.post("/login")
def login(usuario_id: int):
    token = crear_jwt(usuario_id)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/usuario")
def obtener_usuario(token: str):
    datos = verificar_jwt(token)
    if not datos:
        return {"error": "Token inválido"}
    return datos

print("JWT para tokens seguros")
print("Incluye expiración y validación")
"""output
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer"
}
"""
