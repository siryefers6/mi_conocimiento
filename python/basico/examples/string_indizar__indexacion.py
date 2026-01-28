"""
Objetivo: Acceder a caracteres individuales por su posición
Referencia: []
Tipo: operador
Nivel: basico
"""

# acceder por índice
texto = "Hola"
print(f"Carácter 0: {texto[0]}")
print(f"Carácter 1: {texto[1]}")

# índices negativos (desde el final)
print(f"Último carácter: {texto[-1]}")
print(f"Penúltimo: {texto[-2]}")

# cambiar carácter (genera error, strings son inmutables)
# texto[0] = "h"  # Error: TypeError

"""output
Carácter 0: H
Carácter 1: o
Último carácter: a
Penúltimo: l
"""
