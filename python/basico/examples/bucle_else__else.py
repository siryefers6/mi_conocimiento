"""
Objetivo: Ejecutar código después del bucle (si no se rompe)
Referencia: else
Tipo: keyword
Nivel: basico
"""

# else sin break
for i in range(3):
    print(i)
else:
    print("Bucle completado sin break")

print("---")

# else con break
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Esto no se ejecuta")

"""output
0
1
2
Bucle completado sin break
---
0
1
"""
