from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

"""
Objetivo: Habilitar CORS en la aplicación
Referencia: CORSMiddleware
Tipo: Middleware
Nivel: basico
"""

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://ejemplo.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/datos")
def obtener_datos():
    return {"datos": "disponibles"}

print("CORS habilitado para:")
print("- http://localhost:3000")
print("- https://ejemplo.com")
"""output
{
  "datos": "disponibles"
}
"""
