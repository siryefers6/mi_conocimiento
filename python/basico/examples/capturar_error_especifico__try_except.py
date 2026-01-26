"""
Objetivo: capturar distintos tipos de excepciones de manera específica
Referencia: except <Error>
Tipo: keyword
Nivel: basico
"""

try:
    x = int("abc")
except ValueError:
    print("Valor inválido")
except TypeError:
    print("Tipo inválido")

"""output
Valor inválido
"""
