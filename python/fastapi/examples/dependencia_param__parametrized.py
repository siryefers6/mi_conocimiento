from fastapi import FastAPI, Depends

"""
Objetivo: Dependencias con parámetros
Referencia: Depends() con función parametrizada
Tipo: Patrón
Nivel: intermedio
"""

def obtener_usuario_por_token(token: str):
    return {"usuario_id": 1, "token": token}

def verificar_permisos(usuario = Depends(obtener_usuario_por_token)):
    if usuario["usuario_id"] == 1:
        return True
    return False

app = FastAPI()

@app.get("/items")
def listar_items(autorizado: bool = Depends(verificar_permisos)):
    if autorizado:
        return {"items": ["item1", "item2"]}
    return {"error": "No autorizado"}

print("Dependencias parametrizadas")
print("Se pueden encadenar dependencias")
"""output
{
  "items": ["item1", "item2"]
}
"""
