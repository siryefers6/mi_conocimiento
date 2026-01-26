"""
Objetivo: saltar la iteración actual y continuar con la siguiente
Referencia: continue
Tipo: keyword
Nivel: basico
"""

# carga de datos
numeros = [1, 2, 3, 4, 5]

# transformación: imprimir solo números impares
for n in numeros:
    if n % 2 == 0:
        continue
    print(n)

"""output
1
3
5
"""
