from fastapi import FastAPI
from fastapi.middleware.base import BaseHTTPMiddleware

"""
Objetivo: Middleware básico personalizado
Referencia: BaseHTTPMiddleware, dispatch
Tipo: Middleware
Nivel: intermedio
"""

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"Método: {request.method}")
        print(f"Ruta: {request.url.path}")
        response = await call_next(request)
        print(f"Status: {response.status_code}")
        return response

app = FastAPI()
app.add_middleware(LoggingMiddleware)

@app.get("/items")
def listar_items():
    return {"items": []}

print("Middleware básico")
print("Registra métodos, rutas y status codes")
"""output
Método: GET
Ruta: /items
Status: 200
"""
