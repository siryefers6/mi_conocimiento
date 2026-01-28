"""
Objetivo: Cambiar el valor de un elemento en una lista
Referencia: []
Tipo: operador
Nivel: basico
"""

# modificar elemento
numeros = [10, 20, 30]
print("Original:", numeros)

numeros[1] = 25
print("Modificado:", numeros)

# cambiar múltiples
numeros[0] = 5
numeros[-1] = 35
print("Varios cambios:", numeros)

"""output
Original: [10, 20, 30]
Modificado: [10, 25, 30]
Varios cambios: [5, 25, 35]
"""
