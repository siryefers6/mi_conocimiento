"""
Objetivo: Obtener índice y valor de secuencia
Referencia: enumerate
Tipo: función
Nivel: basico
"""

# enumerate simple
frutas = ["manzana", "plátano", "cereza"]
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

print("---")

# enumerate con start
colores = ["rojo", "verde", "azul"]
for i, color in enumerate(colores, 1):
    print(f"{i}: {color}")

"""output
0: manzana
1: plátano
2: cereza
---
1: rojo
2: verde
3: azul
"""
