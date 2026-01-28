"""
Objetivo: Leer todas las líneas como lista
Referencia: readlines
Tipo: método
Nivel: basico
"""

# readlines devuelve lista
import os

# crear archivo
with open("temp.txt", "w") as f:
    f.write("Manzana\nPlátano\nCereza")

# leer líneas
with open("temp.txt", "r") as f:
    lineas = f.readlines()

print(lineas)

# iterar
print("---")
with open("temp.txt", "r") as f:
    for linea in f.readlines():
        print(linea.strip())

# limpiar
if os.path.exists("temp.txt"):
    os.remove("temp.txt")

"""output
['Manzana\n', 'Plátano\n', 'Cereza']
---
Manzana
Plátano
Cereza
"""
