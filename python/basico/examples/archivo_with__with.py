"""
Objetivo: Usar context manager para abrir archivos
Referencia: with
Tipo: keyword
Nivel: basico
"""

# with cierra automáticamente
import os

# escribir con with
with open("temp.txt", "w") as f:
    f.write("Línea 1\nLínea 2")

# leer con with
with open("temp.txt", "r") as f:
    for linea in f:
        print(linea.rstrip())

# archivo se cierra automáticamente

# limpiar
if os.path.exists("temp.txt"):
    os.remove("temp.txt")

"""output
Línea 1
Línea 2
"""
