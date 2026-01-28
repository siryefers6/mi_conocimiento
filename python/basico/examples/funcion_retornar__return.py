"""
Objetivo: Devolver un valor de una función
Referencia: return
Tipo: keyword
Nivel: basico
"""

# función que retorna
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)

# función con condicional
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))
print(es_par(7))

# función que puede retornar None
def procesar(valor):
    if valor > 0:
        return "Positivo"
    return None

print(procesar(5))
print(procesar(-5))

"""output
8
True
False
Positivo
None
"""
