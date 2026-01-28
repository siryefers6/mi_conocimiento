"""
Objetivo: Escribir contenido en un archivo
Referencia: write
Tipo: método
Nivel: basico
"""

# write escribe contenido
import os

# escribir texto
with open("temp.txt", "w") as f:
    f.write("Hola\n")
    f.write("Mundo")

# leer lo escrito
with open("temp.txt", "r") as f:
    print(f.read())

# limpiar
if os.path.exists("temp.txt"):
    os.remove("temp.txt")

"""output
Hola
Mundo
"""
