"""
Objetivo: Leer una línea a la vez
Referencia: readline
Tipo: método
Nivel: basico
"""

# readline lee una línea
import os

# crear archivo
with open("temp.txt", "w") as f:
    f.write("Primera\nSegunda\nTercera")

# leer línea por línea
with open("temp.txt", "r") as f:
    linea1 = f.readline()
    linea2 = f.readline()
    print(linea1.strip())
    print(linea2.strip())

# limpiar
if os.path.exists("temp.txt"):
    os.remove("temp.txt")

"""output
Primera
Segunda
"""
