"""
Objetivo: Usar parámetros con valores por defecto
Referencia: =
Tipo: operador
Nivel: basico
"""

# parámetro con valor por defecto
def saludar(nombre="Mundo"):
    print(f"Hola {nombre}")

saludar()
saludar("Ana")

# múltiples parámetros
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(5))
print(potencia(5, 3))

# valores por defecto
def crear_usuario(nombre, activo=True, rol="usuario"):
    print(f"{nombre}: {activo}, {rol}")

crear_usuario("Juan")
crear_usuario("Ana", False, "admin")

"""output
Hola Mundo
Hola Ana
25
125
Juan: True, usuario
Ana: False, admin
"""
