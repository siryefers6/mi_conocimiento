"""
Objetivo: Obtener una lista ordenada (sin modificar original)
Referencia: sorted
Tipo: función
Nivel: basico
"""

# sorted mantiene original
numeros = [3, 1, 4, 1, 5]
ordenados = sorted(numeros)
print(f"Original: {numeros}")
print(f"Ordenada: {ordenados}")

# sorted descendente
descendente = sorted(numeros, reverse=True)
print(f"Descendente: {descendente}")

# sorted con strings
palabras = ["zebra", "apple", "mango"]
print(sorted(palabras))

"""output
Original: [3, 1, 4, 1, 5]
Ordenada: [1, 1, 3, 4, 5]
Descendente: [5, 4, 3, 1, 1]
['apple', 'mango', 'zebra']
"""
