from fastapi import FastAPI

"""
Objetivo: Documentación automática con OpenAPI
Referencia: /docs, /redoc, /openapi.json
Tipo: Documentación
Nivel: basico
"""

app = FastAPI(
    title="API de Ejemplo",
    description="Documentación automática de FastAPI",
    version="1.0.0"
)

@app.get("/items/{item_id}")
def obtener_item(item_id: int):
    """
    Obtiene un item específico por su ID.
    
    - **item_id**: ID del item a obtener
    """
    return {"item_id": item_id}

print("Documentación disponible en:")
print("- http://localhost:8000/docs (Swagger UI)")
print("- http://localhost:8000/redoc (ReDoc)")
print("- http://localhost:8000/openapi.json (OpenAPI schema)")
"""output
Accesible automáticamente
Generada desde type hints y docstrings
"""
