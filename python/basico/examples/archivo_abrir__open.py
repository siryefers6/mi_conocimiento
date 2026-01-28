"""
Objetivo: Abrir un archivo para lectura o escritura
Referencia: open
Tipo: función
Nivel: basico
"""

# nota: este ejemplo usa ruta simulada
import os

# crear archivo temporal
contenido = "Línea 1\nLínea 2\nLínea 3"
archivo_path = "temp_ejemplo.txt"

# escribir archivo
with open(archivo_path, "w") as f:
    f.write(contenido)

# leer archivo
with open(archivo_path, "r") as f:
    datos = f.read()

print(datos)

# limpiar
if os.path.exists(archivo_path):
    os.remove(archivo_path)

"""output
Línea 1
Línea 2
Línea 3
"""
