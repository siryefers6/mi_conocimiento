"""
Objetivo: Aceptar número variable de argumentos con *args
Referencia: *args
Tipo: parámetro
Nivel: basico
"""

# función con *args
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar(1, 2, 3))
print(sumar(1, 2, 3, 4, 5))

# combinar con parámetros normales
def imprimir(prefijo, *valores):
    print(prefijo, valores)

imprimir("Números:", 1, 2, 3)
imprimir("Letras:", "a", "b", "c")

"""output
6
15
Números: (1, 2, 3)
Letras: ('a', 'b', 'c')
"""
