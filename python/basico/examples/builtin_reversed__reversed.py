"""
Objetivo: Iterar sobre secuencia invertida
Referencia: reversed
Tipo: función
Nivel: basico
"""

# reversed es un iterador
numeros = [1, 2, 3, 4, 5]
print(list(reversed(numeros)))

# usar en for
lista = ["a", "b", "c"]
for elemento in reversed(lista):
    print(elemento)

print("---")

# original no cambia
print(f"Original: {numeros}")

"""output
[5, 4, 3, 2, 1]
c
b
a
---
Original: [1, 2, 3, 4, 5]
"""
