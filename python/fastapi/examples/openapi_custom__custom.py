from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

"""
Objetivo: Personalizar OpenAPI schema
Referencia: openapi() custom function
Tipo: Documentación
Nivel: avanzado
"""

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mi API Personalizada",
        version="2.0.0",
        description="Schema OpenAPI customizado",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://ejemplo.com/logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/items")
def listar_items():
    return []

print("OpenAPI personalizado")
print("Modificar schema según necesidades")
"""output
OpenAPI schema customizado
Logo y metadatos personalizados
"""
