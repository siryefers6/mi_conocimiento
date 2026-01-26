"""
Objetivo: terminar un bucle inmediatamente cuando se cumple una condición
Referencia: break
Tipo: keyword
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3, 4, 5]

# transformación: detener bucle cuando se encuentra un número mayor que 3
for n in numeros:
    if n > 3:
        break
    print(n)

"""output
1
2
3
"""
