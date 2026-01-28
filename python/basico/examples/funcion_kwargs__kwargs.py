"""
Objetivo: Aceptar argumentos nombrados variables con **kwargs
Referencia: **kwargs
Tipo: parámetro
Nivel: basico
"""

# función con **kwargs
def crear_persona(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

crear_persona(nombre="Ana", edad=30, ciudad="Madrid")

print("---")

# combinar args y kwargs
def funcion(a, *args, **kwargs):
    print(f"a: {a}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

funcion(1, 2, 3, nombre="Juan", edad=25)

"""output
nombre: Ana
edad: 30
ciudad: Madrid
---
a: 1
args: (2, 3)
kwargs: {'nombre': 'Juan', 'edad': 25}
"""
