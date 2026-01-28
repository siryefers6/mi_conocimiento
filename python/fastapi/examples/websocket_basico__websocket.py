from fastapi import FastAPI, WebSocket

"""
Objetivo: WebSocket básico
Referencia: WebSocket, accept, send, receive
Tipo: Características avanzadas
Nivel: avanzado
"""

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()

print("WebSocket simple")
print("Conecta con: ws://localhost:8000/ws")
"""output
Cliente envía: "Hola"
Servidor responde: "Echo: Hola"
Conexión bidireccional persistente
"""
