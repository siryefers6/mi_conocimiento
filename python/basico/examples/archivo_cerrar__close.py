"""
Objetivo: Cerrar un archivo manualmente
Referencia: close
Tipo: método
Nivel: basico
"""

# cerrar manual (mejor usar with)
import os

# abrir sin context manager
f = open("temp.txt", "w")
f.write("Contenido")
f.close()  # debe cerrarse

# verificar
with open("temp.txt", "r") as f2:
    print(f2.read())

# limpiar
if os.path.exists("temp.txt"):
    os.remove("temp.txt")

"""output
Contenido
"""
