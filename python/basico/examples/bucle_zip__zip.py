"""
Objetivo: Iterar sobre múltiples listas simultáneamente
Referencia: zip
Tipo: función
Nivel: basico
"""

# zip dos listas
nombres = ["Juan", "Ana", "Carlos"]
edades = [25, 30, 28]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre}: {edad} años")

print("---")

# zip tres listas
letras = ["a", "b", "c"]
numeros = [1, 2, 3]
simbolos = ["!", "@", "#"]

for letra, numero, simbolo in zip(letras, numeros, simbolos):
    print(f"{letra}{numero}{simbolo}")

"""output
Juan: 25 años
Ana: 30 años
Carlos: 28 años
---
a1!
b2@
c3#
"""
