"""
Objetivo: iterar sobre una secuencia obteniendo índice y valor usando enumerate
Referencia: enumerate
Tipo: funcion
Nivel: basico
"""

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
