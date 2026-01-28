"""
Objetivo: Capturar tipos específicos de errores
Referencia: except
Tipo: keyword
Nivel: basico
"""

# except específico
try:
    numero = int("abc")
except ValueError:
    print("ValueError: Conversión no válida")

# otro tipo
try:
    lista = [1, 2]
    print(lista[10])
except IndexError:
    print("IndexError: Índice inválido")

# múltiples except
try:
    valor = None
    print(valor.upper())
except AttributeError:
    print("AttributeError: Atributo no existe")
except TypeError:
    print("TypeError: Tipo incorrecto")

"""output
ValueError: Conversión no válida
IndexError: Índice inválido
AttributeError: Atributo no existe
"""
