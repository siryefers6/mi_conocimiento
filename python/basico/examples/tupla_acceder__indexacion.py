"""
Objetivo: Acceder a elementos de una tupla por índice
Referencia: []
Tipo: operador
Nivel: basico
"""

# acceder por índice
frutas = ("manzana", "plátano", "cereza")
print("Primer elemento:", frutas[0])
print("Segundo elemento:", frutas[1])

# índices negativos
print("Último:", frutas[-1])
print("Penúltimo:", frutas[-2])

# tuplas son inmutables
# frutas[0] = "uva"  # Error: TypeError

"""output
Primer elemento: manzana
Segundo elemento: plátano
Último: cereza
Penúltimo: plátano
"""
