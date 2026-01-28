# app_basica__basico.py
from fastapi import FastAPI

"""
Objetivo: Crear la primera aplicación FastAPI
Referencia: FastAPI, @app.get()
Tipo: Aplicación
Nivel: basico
"""

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "¡Hola FastAPI!"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"saludo": f"Hola {nombre}"}

print("Ejecuta: uvicorn app_basica__basico:app --reload")
"""output
Aplicación ejecutándose en http://localhost:8000
"""
