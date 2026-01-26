"""
Objetivo: capturar una excepción y relanzarla a niveles superiores
Referencia: raise
Tipo: keyword
Nivel: basico
"""

try:
    x = int("abc")
except ValueError as e:
    print("Capturado y relanzando error")
    raise e

"""output
Capturado y relanzando error
Traceback (most recent call last):
  File "re_lanzar_error__try_except.py", line 9, in <module>
    raise e
ValueError: invalid literal for int() with base 10: 'abc'
"""
