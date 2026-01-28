from fastapi import FastAPI, BackgroundTasks

"""
Objetivo: Ejecutar tareas en background
Referencia: BackgroundTasks
Tipo: Características avanzadas
Nivel: intermedio
"""

app = FastAPI()

def procesar_email(email: str):
    print(f"Enviando email a {email}...")
    # Simular procesamiento
    import time
    time.sleep(2)
    print(f"Email enviado a {email}")

@app.post("/enviar-email")
async def enviar_email(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(procesar_email, email)
    return {
        "mensaje": "Email será enviado en background",
        "email": email
    }

print("Background tasks")
print("La respuesta se envía sin esperar a que termine")
"""output
{
  "mensaje": "Email será enviado en background",
  "email": "user@example.com"
}
"""
