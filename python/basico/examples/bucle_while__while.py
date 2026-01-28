"""
Objetivo: Iterar mientras una condición sea verdadera
Referencia: while
Tipo: keyword
Nivel: basico
"""

# while simple
contador = 0
while contador < 3:
    print(contador)
    contador += 1

print("---")

# while con variable booleana
activo = True
numero = 5
while activo and numero > 0:
    print(numero)
    numero -= 1
    if numero == 0:
        activo = False

"""output
0
1
2
---
5
4
3
2
1
"""
