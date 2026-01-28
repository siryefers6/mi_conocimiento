from fastapi import FastAPI
from fastapi.responses import HTMLResponse

"""
Objetivo: Retornar HTML directamente
Referencia: HTMLResponse
Tipo: Respuesta
Nivel: basico
"""

app = FastAPI()

@app.get("/html", response_class=HTMLResponse)
def obtener_html():
    return """
    <html>
        <head>
            <title>FastAPI</title>
        </head>
        <body>
            <h1>Hola desde FastAPI</h1>
            <p>Respuesta HTML</p>
        </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>Bienvenido</h1>"

print("Respuestas HTML")
print("Útil para endpoints que retornan contenido HTML")
"""output
<html>
  <body>
    <h1>Hola desde FastAPI</h1>
  </body>
</html>
"""
