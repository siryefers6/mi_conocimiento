"""
Objetivo: Capturar errores con try-except
Referencia: try
Tipo: keyword
Nivel: basico
"""

# try-except simple
try:
    numero = int("abc")
except:
    print("Error al convertir")

# otro error capturado
try:
    lista = [1, 2, 3]
    print(lista[10])
except:
    print("Índice fuera de rango")

# sin error
try:
    x = 5 + 3
    print(x)
except:
    print("Error")

"""output
Error al convertir
Índice fuera de rango
8
"""
