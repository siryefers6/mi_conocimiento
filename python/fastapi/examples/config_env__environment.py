from fastapi import FastAPI
from pydantic_settings import BaseSettings

"""
Objetivo: Variables de entorno con Pydantic
Referencia: BaseSettings, .env files
Tipo: Configuración
Nivel: intermedio
"""

class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    api_key: str = "secret-key"
    debug: bool = False
    max_connections: int = 10
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
app = FastAPI()

@app.get("/config")
def obtener_config():
    return {
        "database": settings.database_url,
        "debug": settings.debug,
        "max_connections": settings.max_connections
    }

print("Variables de entorno desde .env")
print("DATABASE_URL=postgresql://...")
print("API_KEY=tu-clave")
print("DEBUG=true")
"""output
{
  "database": "postgresql://user:pass@localhost/db",
  "debug": true,
  "max_connections": 10
}
"""
