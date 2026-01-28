from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

"""
Objetivo: Flujo OAuth2 simple
Referencia: OAuth2PasswordBearer, OAuth2PasswordRequestForm
Tipo: Seguridad
Nivel: intermedio
"""

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

usuarios = {
    "juan": {"password": "secret123", "full_name": "Juan Pérez"}
}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = usuarios.get(form_data.username)
    if not usuario or usuario["password"] != form_data.password:
        return {"error": "Credenciales inválidas"}
    return {"access_token": form_data.username, "token_type": "bearer"}

@app.get("/usuario/me")
async def obtener_usuario(token: str = Depends(oauth2_scheme)):
    usuario = usuarios.get(token)
    if not usuario:
        return {"error": "Token inválido"}
    return {"usuario": token, "full_name": usuario["full_name"]}

print("OAuth2 con contraseña")
print("Flujo estándar para aplicaciones web")
"""output
{
  "access_token": "juan",
  "token_type": "bearer"
}
"""
