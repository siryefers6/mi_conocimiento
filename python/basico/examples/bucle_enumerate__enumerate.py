"""
Objetivo: Obtener índice y valor durante iteración
Referencia: enumerate
Tipo: función
Nivel: basico
"""

# enumerate en lista
frutas = ["manzana", "plátano", "cereza"]
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

print("---")

# enumerate con inicio
for i, letra in enumerate("abc", start=1):
    print(f"{i}: {letra}")

"""output
0: manzana
1: plátano
2: cereza
---
1: a
2: b
3: c
"""
