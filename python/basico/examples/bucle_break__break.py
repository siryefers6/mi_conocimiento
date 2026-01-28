"""
Objetivo: Salir del bucle inmediatamente
Referencia: break
Tipo: keyword
Nivel: basico
"""

# break en for
for i in range(10):
    if i == 3:
        break
    print(i)

print("---")

# break en while
contador = 0
while True:
    if contador == 2:
        break
    print(contador)
    contador += 1

"""output
0
1
2
---
0
1
"""
