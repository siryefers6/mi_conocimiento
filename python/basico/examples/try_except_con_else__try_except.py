"""
Objetivo: ejecutar código adicional si no ocurre ninguna excepción
Referencia: try/except/else
Tipo: keyword
Nivel: basico
"""

try:
    x = int("10")
except ValueError:
    print("Valor inválido")
else:
    print("Conversión exitosa:", x)

"""output
Conversión exitosa: 10
"""
