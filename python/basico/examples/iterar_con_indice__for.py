"""
Objetivo: iterar sobre una lista obteniendo índice y valor
Referencia: for / enumerate
Tipo: keyword
Nivel: basico
"""

# imports
# no aplica

# carga de datos
frutas = ["manzana", "banana", "cereza"]

# transformación
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# resultado
# print dentro del bucle produce la salida

"""output
0: manzana
1: banana
2: cereza
"""
