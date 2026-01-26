"""
Objetivo: capturar una excepción y asignarla a una variable para inspección
Referencia: try/except as e
Tipo: keyword
Nivel: basico
"""

try:
    x = int("abc")
except Exception as e:
    print("Error capturado:", e)

"""output
Error capturado: invalid literal for int() with base 10: 'abc'
"""
