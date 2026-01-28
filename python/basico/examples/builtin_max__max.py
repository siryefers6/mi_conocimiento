"""
Objetivo: Encontrar el valor máximo
Referencia: max
Tipo: función
Nivel: basico
"""

# máximo de lista
numeros = [3, 1, 4, 1, 5, 9]
maximo = max(numeros)
print(f"Máximo: {maximo}")

# máximo de strings
palabras = ["hola", "mundo", "python"]
mas_larga = max(palabras, key=len)
print(f"Más larga: {mas_larga}")

# máximo de múltiples valores
print(max(10, 20, 5))

"""output
Máximo: 9
Más larga: python
20
"""
