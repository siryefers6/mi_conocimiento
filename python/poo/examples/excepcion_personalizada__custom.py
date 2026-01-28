"""
Objetivo: Crear excepciones personalizadas
Referencia: class Error(Exception)
Tipo: clase
Nivel: basico
"""

class ErrorEdad(Exception):
    pass

class Persona:
    def __init__(self, nombre, edad):
        if edad < 0:
            raise ErrorEdad("La edad no puede ser negativa")
        self.nombre = nombre
        self.edad = edad

try:
    p1 = Persona("Ana", 30)
    print(f"{p1.nombre} tiene {p1.edad} años")
    
    p2 = Persona("Juan", -5)
except ErrorEdad as e:
    print(f"Error personalizado: {e}")

"""output
Ana tiene 30 años
Error personalizado: La edad no puede ser negativa
"""
