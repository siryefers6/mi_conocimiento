from fastapi import FastAPI
from contextlib import asynccontextmanager

"""
Objetivo: Eventos de inicio y cierre
Referencia: lifespan, startup/shutdown events
Tipo: Características avanzadas
Nivel: intermedio
"""

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Aplicación iniciando...")
    # Setup
    yield
    # Cleanup
    print("Aplicación cerrando...")

app = FastAPI(lifespan=lifespan)

@app.get("/items")
def listar_items():
    return []

print("Lifespan events")
print("Ejecuta código al inicio y cierre")
"""output
Aplicación iniciando...
(endpoints disponibles)
Aplicación cerrando...
"""
