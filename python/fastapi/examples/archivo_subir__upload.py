from fastapi import FastAPI, File, UploadFile

"""
Objetivo: Subir archivos
Referencia: UploadFile, File()
Tipo: Formulario
Nivel: intermedio
"""

app = FastAPI()

@app.post("/subir-archivo")
async def subir_archivo(archivo: UploadFile = File(...)):
    contenido = await archivo.read()
    return {
        "filename": archivo.filename,
        "content_type": archivo.content_type,
        "tamaño": len(contenido)
    }

@app.post("/multiples-archivos")
async def subir_multiples(archivos: list[UploadFile] = File(...)):
    return {
        "archivos": [a.filename for a in archivos],
        "cantidad": len(archivos)
    }

print("POST /subir-archivo con multipart/form-data")
print("Maneja archivos binarios")
"""output
{
  "filename": "documento.pdf",
  "content_type": "application/pdf",
  "tamaño": 1024
}
"""
