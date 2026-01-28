"""
Objetivo: Saltar a la siguiente iteración del bucle
Referencia: continue
Tipo: keyword
Nivel: basico
"""

# continue en for
for i in range(5):
    if i == 2:
        continue
    print(i)

print("---")

# continue con condición
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2 == 0:
        continue
    print(numero)

"""output
0
1
3
4
---
1
3
5
"""
