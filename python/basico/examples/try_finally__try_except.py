"""
Objetivo: ejecutar un bloque de código siempre, haya o no excepción
Referencia: try/finally
Tipo: keyword
Nivel: basico
"""

try:
    x = 10 / 0
finally:
    print("Este bloque siempre se ejecuta")

"""output
Este bloque siempre se ejecuta
"""
