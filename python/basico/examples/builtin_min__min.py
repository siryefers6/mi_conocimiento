"""
Objetivo: Encontrar el valor mínimo
Referencia: min
Tipo: función
Nivel: basico
"""

# mínimo de lista
numeros = [3, 1, 4, 1, 5, 9]
minimo = min(numeros)
print(f"Mínimo: {minimo}")

# mínimo de strings
palabras = ["hola", "mundo", "a"]
mas_corta = min(palabras, key=len)
print(f"Más corta: {mas_corta}")

# mínimo de valores
print(min(10, 20, 5))

"""output
Mínimo: 1
Más corta: a
5
"""
