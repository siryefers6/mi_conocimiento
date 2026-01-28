"""
Objetivo: Definir una función reutilizable
Referencia: def
Tipo: keyword
Nivel: basico
"""

# función simple sin parámetros
def saludar():
    print("Hola")

saludar()

# función con parámetro
def saludar_persona(nombre):
    print(f"Hola {nombre}")

saludar_persona("Ana")

# función con múltiples parámetros
def suma(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

suma(5, 3)

"""output
Hola
Hola Ana
5 + 3 = 8
"""
