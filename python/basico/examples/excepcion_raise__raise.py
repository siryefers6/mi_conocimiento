"""
Objetivo: Lanzar una excepción
Referencia: raise
Tipo: keyword
Nivel: basico
"""

# raise lanza error
def validar_edad(edad):
    if edad < 0:
        raise ValueError("Edad no puede ser negativa")
    return edad

# con error
try:
    validar_edad(-5)
except ValueError as e:
    print(f"Error: {e}")

# sin error
try:
    resultado = validar_edad(25)
    print(f"Edad válida: {resultado}")
except ValueError as e:
    print(f"Error: {e}")

"""output
Error: Edad no puede ser negativa
Edad válida: 25
"""
