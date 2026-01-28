from fastapi import FastAPI
from fastapi.responses import StreamingResponse

"""
Objetivo: Streaming de respuestas
Referencia: StreamingResponse, generators
Tipo: Características avanzadas
Nivel: avanzado
"""

app = FastAPI()

def generar():
    for i in range(5):
        yield f"data: Item {i}\n"

@app.get("/stream")
async def stream_items():
    return StreamingResponse(
        generar(),
        media_type="text/event-stream"
    )

@app.get("/descargar")
async def descargar_archivo():
    def iterfile():
        with open("archivo.txt", mode="rb") as file_like:
            yield file_like.read()
    return StreamingResponse(
        iterfile(),
        media_type="application/octet-stream",
        headers={"Content-Disposition": "attachment; filename=archivo.txt"}
    )

print("Streaming de datos")
print("Útil para archivos grandes o Server-Sent Events")
"""output
Streaming respuesta
Datos entregados en chunks
"""
