"""
Objetivo: Leer todo el contenido de un archivo
Referencia: read
Tipo: método
Nivel: basico
"""

# leer completo
import os

# crear archivo temporal
with open("temp.txt", "w") as f:
    f.write("Línea 1\nLínea 2\nLínea 3")

# leer completo
with open("temp.txt", "r") as f:
    contenido = f.read()

print(contenido)

# limpiar
if os.path.exists("temp.txt"):
    os.remove("temp.txt")

"""output
Línea 1
Línea 2
Línea 3
"""
