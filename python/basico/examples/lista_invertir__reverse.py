"""
Objetivo: Invertir el orden de los elementos en una lista
Referencia: reverse
Tipo: método
Nivel: basico
"""

# invertir lista
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print("Invertida:", numeros)

# invertir strings
palabras = ["a", "b", "c"]
palabras.reverse()
print("Palabras:", palabras)

# invertir lista con slicing (no modifica original)
original = [10, 20, 30]
invertida = original[::-1]
print("Original:", original)
print("Invertida:", invertida)

"""output
Invertida: [5, 4, 3, 2, 1]
Palabras: ['c', 'b', 'a']
Original: [10, 20, 30]
Invertida: [30, 20, 10]
"""
