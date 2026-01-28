from fastapi import FastAPI
from fastapi.middleware.base import BaseHTTPMiddleware
import time

"""
Objetivo: Crear middleware personalizado
Referencia: BaseHTTPMiddleware
Tipo: Middleware
Nivel: intermedio
"""

class TimingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        inicio = time.time()
        response = await call_next(request)
        duracion = time.time() - inicio
        response.headers["X-Process-Time"] = str(duracion)
        return response

app = FastAPI()
app.add_middleware(TimingMiddleware)

@app.get("/items")
def listar_items():
    return [{"id": 1}, {"id": 2}]

print("Middleware de timing")
print("Agrega header X-Process-Time con duración")
"""output
{
  "headers": {
    "X-Process-Time": "0.001234"
  },
  "items": [{"id": 1}, {"id": 2}]
}
"""
