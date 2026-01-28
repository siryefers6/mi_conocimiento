from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

"""
Objetivo: Configurar CORS avanzado
Referencia: CORSMiddleware with multiple options
Tipo: Middleware
Nivel: intermedio
"""

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://ejemplo.com",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
    expose_headers=["X-Total-Count"],
    max_age=600,
)

@app.get("/datos")
def obtener_datos():
    return {"datos": "disponibles"}

print("CORS avanzado configurado")
print("Allow-Credentials: true")
print("Max-Age: 600 segundos")
"""output
{
  "datos": "disponibles"
}
"""
