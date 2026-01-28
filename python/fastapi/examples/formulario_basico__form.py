from fastapi import FastAPI, Form

"""
Objetivo: Recibir datos de formularios HTML
Referencia: Form()
Tipo: Formulario
Nivel: basico
"""

app = FastAPI()

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {
        "username": username,
        "autenticado": True
    }

@app.post("/comentario")
async def crear_comentario(
    texto: str = Form(...),
    autor: str = Form(...),
    activo: bool = Form(True)
):
    return {
        "texto": texto,
        "autor": autor,
        "activo": activo
    }

print("POST /login con form-data")
print("Parámetros enviados como formulario HTML tradicional")
"""output
{
  "username": "juan",
  "autenticado": true
}
"""
